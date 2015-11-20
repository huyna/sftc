/*
 * debug.h
 *
 *  Created on: April 7, 2009
 *      Author: Daniel Moran & Gal Diskin
 */

#ifndef DEBUG___H___
#define DEBUG___H___

//#define __DEBUG 1
#ifdef __DEBUG
#define DEBUG_PRINT printf
#else
#define DEBUG_PRINT(...)
#endif

#endif
