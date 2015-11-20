/*
 * RC4.h
 *
 *  Created on: Mar 28, 2009
 *      Author: Daniel Moran & Gal Diskin
 */

#ifndef RC4_H_
#define RC4_H_

int initialize(const unsigned int keylen);
unsigned int setkeylen(const unsigned int keylen);
unsigned int getkeylen();

void rc4_init(const unsigned char *key);
unsigned char rc4_output();
void rc4_destroy();
unsigned rc4_reset();
unsigned int rc4_getJ();
unsigned int rc4_getI();
unsigned char * rc4_getS();
unsigned char* rc4_getKey();
unsigned rc4_getCounter();
unsigned char *rc4_encrypt(const unsigned char *text);
int rc4_test_key(unsigned char* key);

#endif /* RC4_H_ */
