/*
 * main.c
 *  Running algorithm described in the paper.
 *
 *  Created on: Apr 8, 2009
 *      Author: Daniel Moran & Gal Diskin
 */


//#include "RC4.h"
#include <stdio.h>
#include <stdlib.h>
#include "attack.h"
#include "RC4.h"
#include "debug.h"
#include "our_types.h"

int main(int argc, char* argv[]){
	int keylen;
	if(argc!=2){
		printf("Usage:\nattack keylen\n");
		exit(1);
	}
	keylen=atoi(argv[1]);
	initialize(keylen);
	init_attack();
	BYTE* key=generate_random_key();
	key[0]=0x4f;
	key[1]=0x80;
	key[2]=0x78;
	key[3]=0x29;
	key[4]=0x16;
	printf("Working with key: ");
	print_key(key);printf("\n");
	rc4_init(key);
	BYTE *S=rc4_getS();
	for(int i=0; i<256; ++i){
		printf("%02X ",S[i]);
	}
	printf("\n");
	BYTE* res=FIND_KEY(S);//Main call to algorithm
	if(res == NULL){
		printf("Couldn't guess the key\n");
	}else{
		printf("Our guess: ");
		print_key(res);printf("\n");
	}


	deinit_attack();
	return 1;
}
