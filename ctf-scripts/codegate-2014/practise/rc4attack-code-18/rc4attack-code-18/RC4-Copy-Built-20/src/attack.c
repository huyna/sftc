/*
 * attack.c
 *  Implementation of API of the algorithm.
 *
 *  Created on: Apr 8, 2009
 *      Author: Daniel Moran & Gal Diskin
 */

#include <stdlib.h>
#include <stdio.h>
#include "debug.h"
#include "attack.h"
#include "RC4.h"
#include "hashtable.h"
#include "our_types.h"

static struct hash_table table;

BYTE* generate_random_key(){
	unsigned int key_length=getkeylen();
	BYTE *str=(BYTE*)malloc(sizeof(BYTE)*(key_length+1));
	if(str==NULL){
		return NULL;
	}
	unsigned int i;
	for(i=0;i<key_length;++i){
		str[i]=rand() % 256;            //TOOD: (later) will this generate a uniform distribution?
		DEBUG_PRINT("%02X",str[i]);
	}
	str[i]=0;
	DEBUG_PRINT("\n");
	return str;
}

void print_key(BYTE* str){
	unsigned int key_length=getkeylen();
	unsigned int i;
	for(i=0; i<key_length; ++i){
		printf("%02X",str[i]);
	}
}

//Hash function
uint32_t hash(void *data, size_t key_len)
{
	void *key=data;
	uint32_t hash=0;
	size_t i;

	/* We don't use the key_len arg */
	key_len=sizeof(unsigned);

	for (i=0; i < key_len; i++){
		hash+=*((BYTE *)key+i);
		hash+=hash<<10;
		hash^=hash>>6;
	}

	hash+=hash<<3;
	hash^=hash>>11;
	hash+=hash<<15;

	return hash;
}

int cmp(const void *p1, const void *p2){
	return(p1==p2);
}

void init_attack(){
	//struct hash_table table; // for sum_bytes_i_to_j
	hash_table_init(&table,256,hash,cmp);

}

void deinit_attack(){
	hash_table_free(&table,NULL);
}

// sum key bytes i to j - K[i...j]
// this function automatically wraps around if we reached the end of K
// input  = initial permutation S, indices i and j to sum in between (and incl.)
// output = the sum
// Note: multiple loops around S will not work! i=0 j =511 will only return the same as i=0 j=255
//TODO: (later) should we cache results so as not to repeat calculations?

BYTE_SUM sum_bytes_i_to_j(BYTE* S, INDEX i, INDEX j)
{
	// local vars
	BYTE_SUM res = 0;
	//make sure we get
	i = i & P_SIZE_FOR_BINARIC_AND; //i % P_SIZE;
	j = j & P_SIZE_FOR_BINARIC_AND; //j % P_SIZE;
	unsigned int key= i;
	key<<=8;
	key+=j;
	BYTE_SUM* r=(long*)hash_table_search(&table,&key,0);
	if(r){
		return *r;
	}

	//do the actual loop
	//for (int pos = i; pos != j; pos = ++pos % P_SIZE)
	for (int pos = i;
		 pos != j;
	     )
	{
        res += S[pos];
        ++pos;
        pos &= P_SIZE_FOR_BINARIC_AND;

	}

	//sum should include the j's cell if i!=j
	if (i != j)	res += S[j];
	hash_table_insert(&table,&res,0);

	return res;
}

