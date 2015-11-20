/*
 * write some description here...
 */


/*
 * Includes
 */
#include <stdio.h>
#include "debug.h"
#include "our_types.h"
#include "attack.h"
#include "malloc.h"
#include "matrix.h"
#include "matrix2.h"
#include "determinant.h"
#include "RC4.h"
#include "list.h"


static long count_guesses=0;
static long count_bad_matrix=0;
static unsigned int key_length=5;


/*
 * Variables
 */
//TODO: define S as a global - all functions refer to it and its passed too much, costing too much time.




/*
 * Functions
 */

// This is the main part of the algorithm
// input  = initial permutation,
// output = null on failure to retrieve the key
//          or an array containing a guessed key

//FIXME: add GLOBALFUNC, my eclipse goes crazy when i use a define to in function type
BYTE* FIND_KEY(BYTE* S)
{
	//C[i] --- + probability with it.
	SIGNED_BYTE C[P_SIZE] = {0};
	SIGNED_BYTE C_bar[P_SIZE] = {0};

	get_C_i(S, C, C_bar);                         //fill the C and C_bar arrays


	//find the probability of each optional sum of key bytes
	//TODO: (later) currently we only take the best guess
	list *current_guesses=list_init();
	byte_sum_guess_t *initial_guess=(byte_sum_guess_t*)malloc(sizeof(byte_sum_guess_t));
	initial_guess->i1 = 0;
	initial_guess->i2 = key_length-1;
	initial_guess->value = find_best_guess_for_s(S); //is this according to the end of 4.3 - any sum of l consecutive bytes indicates a guess for S
	initial_guess->w = 255;
	list_add(current_guesses,initial_guess);



	// initialize counters
	// TODO: find_best_guess_for_S should be removed, first guess should come from here as
	//       well...
	BYTE_SUM cur_guess;
	list *guesses=list_init();

	for (int left = 0; left < key_length - 1; ++left)
		for (int right = left; right < key_length -1; ++right)
		{
			// find guesses for the range from left to right.
			// insert wisely == don't
			unsigned int base = 0; // current position in S (multiples of key length)
			//list of guesses for the current values of left and right
			list *cur_val_list=list_init();


			while (base + right < P_SIZE){
				cur_guess=C[base + right];
				if(base+left>0){
					cur_guess -=C[base + left -1];
				}
				cur_guess %= P_SIZE;
				if(cur_guess<0){
					cur_guess+=P_SIZE;
				}
				//try to find value in list
				list_node *tmp=list_head(cur_val_list);
				for (; tmp!=NULL; tmp = list_node_next(tmp)){
					if (list_node_data_ptr(tmp,byte_sum_guess_t)->value == cur_guess){
						++(list_node_data_ptr(tmp,byte_sum_guess_t)->w);
						break;
					}
				}
				if(tmp==NULL){
					// couldn't find in list, enter new element to list
					byte_sum_guess_t *guess = (byte_sum_guess_t *)malloc(sizeof(byte_sum_guess_t));
					guess->i1 = left;
					guess->i2 = right;
					guess->w = 1;
					guess->value = cur_guess;
					list_add(cur_val_list,guess);
				}
				base += key_length;
			} // while

			//Insert elements from cur_val_list to guesses
			list_node *tmp=list_head(cur_val_list);
			for (; tmp!=NULL; tmp = list_node_next(tmp)){
				list_node *iter=list_head(guesses);
				if(iter==NULL){
					list_add(guesses,list_node_data_ptr(tmp,byte_sum_guess_t));
					continue;
				}
				for(;iter!=NULL ;iter=list_node_next(iter)){
					if(list_node_data_ptr(iter,byte_sum_guess_t)->w <= list_node_data_ptr(tmp,byte_sum_guess_t)->w){
						list_add_before(guesses,iter,list_node_data_ptr(tmp,byte_sum_guess_t));
						break;
					}
				}
				if(iter==NULL){
					list_add_tail(guesses, list_node_data_ptr(tmp,byte_sum_guess_t));
				}
			}
			list_free(cur_val_list,NULL);
		} // for

	//we'll start by setting weights by "majority vote" and we'll later move to
	//assigning them according to the probability estimates (theorems 2 and 3)
	//see section 4.2


	BYTE* ret = RECURSIVE_SUBROUTINE(1, current_guesses, guesses, list_head(guesses));
	DEBUG_PRINT("Number of guesses is %ld\nNumber of bad matrices %ld\n",count_guesses,count_bad_matrix);
	//note: * (intution) we'll probably want to start working with rec-subroutine searching for the sums of a single key-byte
	//        and going up to sums of 2,3 until l-1 key bytes (so that the stage with the "many" guesses is at the start of our recursion
	//      * another option is to reverse it (it will possibly make our guesses better - again this is only intuition)
	//      * a third option is to go for the keys where we have more possible guesses (based on the question if the length of the sum is
	//        a generator of the additive group of 255 (again intuition mostly)

	//safety - return null
	return ret;
}



// This is the real main part of the algorithm
// input  = t - index of current sum to be guessed (0 to l where l means end)
//          cur_guess - current guess (linked list, starting with initial guess)
// output = NULL while didn't succeed or the key if found it.

//FIXME: add LOCALFUNC? (OR GLOBAL?)
BYTE* RECURSIVE_SUBROUTINE(BYTE t, list *cur_guess, list *guesses, list_node *first_guess)
{
	if ( t == key_length)
	{
		unsigned char* key=NULL;
		// generate key from the cur_guess (push guesses into a matrix and use some matrix solving library?)
		MAT* A;
		VEC *x,*b;
		PERM* pivot;
		A=m_get(key_length,key_length);
		b=v_get(key_length);
		x=v_get(key_length);
		int c=0,r=0;
		for(list_node* iter=list_head(cur_guess); iter != NULL && r<key_length; iter=list_node_next(iter)){
			for(c=list_node_data_ptr(iter,byte_sum_guess_t)->i1;
				c <= list_node_data_ptr(iter,byte_sum_guess_t)->i2;
				++c){
				A->me[r][c]=1;
			}
			b->ve[r]=list_node_data_ptr(iter,byte_sum_guess_t)->value;
			++r;
		}
		//Calculate matrix determinant
		SQRMATRIX A_det;
		SQRMATRIX_CreateMatrix(&A_det,key_length);
		for(r=0;r<key_length;++r){
			for(c=0;c<key_length;++c){
				A_det.array[r][c]=A->me[r][c];
			}
		}
		int det;
		det=SQRMATRIX_CalcDeterminant(&A_det);
		//TODO: return this later
		SQRMATRIX_DestroyMatrix(&A_det);
		if(det==0){//If determinant is 0 continue to next guess
			++count_bad_matrix;
#ifdef __DEBUG
			//SQRMATRIX_DisplayMatrix(&A_det);
			v_output(b);
			DEBUG_PRINT("Matrix determinant is 0\n");
#endif
			
		}else{
			++count_guesses;
			pivot = px_get(A->m);
			LUfactor(A,pivot);

			x=LUsolve(A,pivot,b,VNULL);
			PX_FREE(pivot);
			//test key (use our RC4 impl)
			key=(unsigned char*)malloc(sizeof(unsigned char)*key_length);
			for(int i=0;i<key_length;++i){
				key[i]=x->ve[i];
			}

			int res=rc4_test_key(key);
			if(res){
				printf("MAZAL TOV! we got the right key.\n");
				print_key(key);
				printf("\n");
			}else{
				//printf("Tried key: ");
				//print_key(key);
				//printf(".");
				free(key);key=NULL;
			}
		}
		//release matrix vars
		M_FREE(A);
		V_FREE(x);
		V_FREE(b);
		return key;
	}

	byte_sum_guess_t cur;
	//list *new_list_head=guesses;


	//TODO: (later) add a for loop running along the "lambeda_t" values here, for the initial impl we'll try the best guess
	//for ()
	//{
	for(int i=0; i<LAMBDA_T; ++i){
		cur = *(list_node_data_ptr(first_guess, byte_sum_guess_t));
		list_node *biatch = list_add_head(cur_guess, &cur);
		BYTE* res=RECURSIVE_SUBROUTINE(t+1, cur_guess, guesses, list_node_next(first_guess));
		if(res!=NULL){
			return res;
		}
		list_del(cur_guess,biatch);
		first_guess = list_node_next(first_guess);
	}
	return NULL;

	//TODO: do something to find the next guess and link it to the current guess
	//when I say something I mean find best guess (i.e best weight) of all the guesses that give us new information
	//(i.e not linearily dependent in our byte values and sums matrix that can be deduced from the cur_guess)
	//see also the note above (intuition)

	//IMPORTANT!
	//explaination how cur_guess is a matrix: each entry in cur_guess contains a list of bytes that are part of the sum and a
	//guess as to the value of the sum. if this matrix is solvable then solving it should give us a value for each byte of the
	//key thus the entire key
	//note: we probably should change cur_guess to a smarter database (for example a (L)x(L+1) matrix as an array?) but we
	//need to consider that we need to keep the ability to backtrack without making it too expensive



	//TODO: if weight of the guess is too small -> return FAIL (section 4.6)


	//These are based on section 4.4
	//correct suggestions (this can be done later, basic alg should work without it)
	//adjust weights (this can be done later, basic alg should work without it)

	//merge counters (section 4.2), also skip for initial impl? need to check


	//go to next iteration in the recurtion
    //RECURSIVE_SUBROUTINE(t+1, cur_guess, );

	//} end of for

}



// This function computes the values of C[i] and C_bar[i] for all i, accroding to the values of S
// input  = initial permutation S, pointers to C and C_bar arrays
// output = C and C_bar arrays are filled with values

//FIXME: add LOCALFUNC, my eclipse goes crazy when i use a define to in function type
VOID get_C_i(BYTE* S, SIGNED_BYTE* C, SIGNED_BYTE* C_bar){
	for(int i=0; i < P_SIZE; ++i){
		//Compute C[i], C'[i]
		C[i] = S[i] - (i*(i+1))/2;                //calculate C[i] by its official formula
		C_bar[i] = S[P_SIZE - i -1] - (i*(i+1))/2;   //calculate C_bar[i] according to its formula
		//TODO: make sure S^(-1) is the reverse of S
	}
	return;
}



// as the name implies - find the best guess for s = the sum of key bytes
// input  = initial permutation S
// output = the best guess we could find for the sum of key bytes
// Note: we need to refine this function later to support getting less than optimal values \ return a list of values
//TODO: implement guesses based on 2*s, 3*s, etc... - this is not high priority (end of section 4.3)

//FIXME: add LOCALFUNC, my eclipse goes crazy when i use a define to in function type
BYTE_SUM find_best_guess_for_s(BYTE* S)
{
	//TODO: replace this array with a hash table or a linked list
	unsigned int *guess_count=(unsigned int*)malloc(sizeof(unsigned int)*255*key_length);
    //index is the guess, value is the number of times it occured

	BYTE_SUM max_guess = 0;
	unsigned int max_count = 0;

	BYTE_SUM cur_guess;

    for (int i=0; i < P_SIZE; i++)
    {
    	//get cur guess
    	cur_guess = sum_bytes_i_to_j(S, i, i + key_length - 1);

    	// increase count for this guess and if its the most common guess, save it until a better guess shows up
    	if ( ( ++(guess_count[cur_guess]) ) > max_count )
    	{
    		max_count = guess_count[cur_guess];
    		max_guess = cur_guess;
    	}
    }
    free(guess_count);
    return max_guess;
}
