/*
 * RC4.c
 *
 *  Created on: Mar 28, 2009
 *      Author: Daniel Moran & Gal Diskin
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <time.h>
#include "RC4.h"
#include "debug.h"
#include "our_types.h"

static BYTE * theKey;			//the key
static unsigned counter; //"age" counter (bytes produced)

static BYTE S[256]; //table
static unsigned int i, j; //pointers

static unsigned int key_length;

unsigned int setkeylen(const unsigned int keylen){
	key_length=keylen;
	return key_length;
}

int initialize(const unsigned int keylen){
	srand(time(NULL));
	DEBUG_PRINT("Initializing with key_length: %d\n",keylen);
	setkeylen(keylen);
	return 0;
}


unsigned int getkeylen(){
	return key_length;
}

/* KSA */
void rc4_init(const BYTE *key){
	if(theKey){
		DEBUG_PRINT("rc4_init => freeing old key");
		free(theKey);
	}
	theKey=(BYTE*)malloc(sizeof(BYTE)*key_length);
	memcpy((void*)theKey,(void*)key,sizeof(BYTE)*key_length);
	//strcpy(theKey,key);
	//initialize S table
	for(i = 0;i < 256;i++){
		S[i] = i;
	}
	//modify S according to the key
	for(i = j = 0;i < 256;i++){
		BYTE temp; //for swapping
		//calculate next j
		j = (j + key[i % key_length] + S[i]) & 255;
		//swap
		temp = S[i];
		S[i] = S[j];
		S[j] = temp;
	}
	//reset global i and j pointers
	i = j = 0;
}

BYTE rc4_output(){
	//for swapping
	BYTE temp;
	//increase global "age" counter
	counter++;
	//move i,j pointers
	i = (i + 1) & 255;
	j = (j + S[i]) & 255;
	//swap i,j cells
	temp = S[i];
	S[i] = S[j];
	S[j] = temp;
	//return next byte for encryption
	return S[(S[i] + S[j]) & 255];
}

void rc4_destroy(){
	DEBUG_PRINT("RC4> destroy\n");
	free(theKey);
}

unsigned rc4_reset(){
	DEBUG_PRINT("RC4> reset - age in bytes %d\n", counter);
	//save output
	unsigned res = counter;
	//reset global counter
	counter = 0;
	//re-initialize
	rc4_init(theKey);
	//return number of reads
	return res;
}

BYTE *rc4_encrypt(const BYTE *text){
	//find text length
	unsigned int len = 0;
	while(*(text + len)){++len;}
	//get memory for result
	BYTE *res = (BYTE*)malloc(sizeof(BYTE)*len);
	if(!res){
		DEBUG_PRINT("RC4_encrypt--> Couldn't allocate memory for encrypted text\n");
		return NULL;
	}
	//encrypt
	unsigned int i = 0;
	for(; i < len; ++i){
		//get next byte in encryption stream
		BYTE next = rc4_output();
		//encrypt
		BYTE encrypted = (text[i] ^ next);
		DEBUG_PRINT("RC4> Encrypting %c=%02X with %c=%02X => %c=%02X\n",
				text[i],text[i],next,next,encrypted,encrypted);
		//save output
		res[i] = encrypted;
	}
	DEBUG_PRINT("\n");
	//set last value to in output to null
	res[len] = 0;
	return res;
}


//GETTERS

unsigned rc4_getCounter() {
	return counter;
}

BYTE * rc4_getS(){
	return S;
}

unsigned int rc4_getI(){
	return i;
}

unsigned int rc4_getJ(){
	return j;
}

int rc4_test_key(unsigned char* key){
	for(int i=0;i<key_length;++i){
		if(theKey[i]!=key[i]){return 0;}
	}
	return 1;
}

BYTE* rc4_getKey(){
	return theKey;
}
