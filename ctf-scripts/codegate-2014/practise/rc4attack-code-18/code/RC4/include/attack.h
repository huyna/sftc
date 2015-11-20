#ifndef ___ATTACK_H__
#define ___ATTACK_H__

#include "our_types.h"
#include "RC4.h"
#include "list.h"

/*
 * Defines
 */
//size of a permutation
#define P_SIZE 256
#define P_SIZE_FOR_BINARIC_AND 0xff

unsigned char* generate_random_key();
void print_key(unsigned char* str);
void init_attack();
void deinit_attack();

GLOBALFUNC BYTE* FIND_KEY(BYTE* S);
VOID get_C_i(BYTE* S, SIGNED_BYTE* C, SIGNED_BYTE* C_bar);
BYTE_SUM find_best_guess_for_s(BYTE* S);
BYTE_SUM sum_bytes_i_to_j(BYTE* S, INDEX i, INDEX j);
BYTE* RECURSIVE_SUBROUTINE(BYTE t, list *cur_guess, list *guesses, list_node *first_guess);


#endif
