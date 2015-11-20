//============================================================================
// Name        : RC4.cpp
// Author      : Daniel Moran & Gal Diskin
// Version     :
// Copyright   : Delerium Software
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include "RC4.h"
using namespace std;

int main(int argc, BYTE* argv[])
{
	//sanity check
	if(argc != 3)
	{
		printf("Usage: \n");
		printf("   RC4 key phrase\n");
		return 0;
	}


	//encryption
	RC4Cipher rc4(argv[1]);
	BYTE* text=argv[2];

	printf("Encrypting text: %s\n",text);

	BYTE* encrypted=rc4.encrypt(text);
	printf("Encrypted text: ");
	for(unsigned int i=0;encrypted[i];++i)
	{
		printf("%02X ",encrypted[i]);
	}
	printf("\n\n");


	//decryption
	printf("Decrypting the encrypted text\n");

	rc4.reset();
	BYTE* res = rc4.encrypt(encrypted);

	printf("Decrypted text: %s\n", res);
	for(unsigned int i=0; res[i]; ++i)
	{
		printf("%02X ", res[i]);
	}
	printf("\n\n");


	return 0;
}
