#ifndef _OUR_TYPES_H
#define _OUR_TYPES_H

/*
 * types.h
 *
 *  Created on: May 11, 2009
 *      Author: Gal Diskin
 */

/* we will redeclare types as defines to allow for easier changing if the need arises */

//
/// Aliases for types
//

//we can change it to double or whatever if need be
#define FRAC float

#define BYTE unsigned char

#define BYTE_SUM long
#define INDEX long
#define WEIGHT long

//probably a short will do instead of int
#define SIGNED_BYTE int

#define VOID void

#define GLOBALFUNC extern
#define GLOBALVAR /**/

#define LOCALFUNC /**/
#define LOCALVAR  /**/

#define INLINE inline

//Number of guesses on each stage
#define LAMBDA_T 80

//#define NULL 0




//
/// real typedefs
//

typedef struct byte_sum_guess
{
    BYTE_SUM value;  //the value we're assuming is the sum K[i1...i2]
    BYTE i1, i2;     //borders for the sum
    WEIGHT w;        //estimated probability (weight)
    //struct byte_sum_guess *next;  //pointer to next best guess

} byte_sum_guess_t;



#endif   //#ifndef _OUR_TYPES_H
