#include <stdio.h>
#include <malloc.h>
#include "determinant.h"
#include <math.h>


		// main( )
/*int main( )
{
	SQRMATRIX p;
	int order;

	printf("Enter order of matrix: ");
	scanf("%d", &order );

	if( !CreateMatrix( &p, order ))
	{
		printf("Matrix couldn't be created.");
		return 0;
	}

	printf("Matrix created.\n\n");
	InputMatrix( &p );

	printf("\nThe matrix is:\n");
	DisplayMatrix( &p );

	printf("\nThe determinant of the matrix is: %d", CalcDeterminant( &p ));

	getch( );
	return 0;
}*/

		// Create matrix of specified order
int SQRMATRIX_CreateMatrix( SQRMATRIX *p, int order )
{
	int i;

	if( order < 1 )
		return 0;

 	p->order = order;
	p->array = (int**) malloc( order * sizeof( int* ));	// Allocate space for each row

	if( !p->array )
		return 0;

	for( i=0; i < order; i++ )
	{
	 	p->array[i] = (int*) malloc( order* sizeof( int ));	// Allocate space for each column
	 	if( !p->array )
	 		return 0;
	 }
	 return 1;
}

		 // Print matrix in proper format
void SQRMATRIX_DisplayMatrix( SQRMATRIX *p )
{
	int i,j;

	if( p->order < 1 )
		return;

	for( i = 0; i < p->order; i++ )
	{
		for( j = 0; j < p->order; j++ )
			printf("%5d ", p->array[i][j] );

		printf("\n");
	}
}

		// Input matrix from user
void SQRMATRIX_InputMatrix( SQRMATRIX *p )
{
	int i,j;

	for( i = 0; i < p->order; i++ )
		for( j = 0; j < p->order; j++ )
		{
			printf("Enter element at ( %d, %d ): ", i+1, j+1 );
			scanf("%d", &p->array[i][j] );
		}
}

/* Calculate the 'minor' of the given matrix at given position.
 The minor is the matrix formed by deleting the specified row
 and column from the matrix.
*/

int SQRMATRIX_CalcMinor( SQRMATRIX *p, SQRMATRIX *minor, int row, int col )
{
	int i,j,a,b;

	if( p->order <= 1 )
		return 0;

	if( row >= p->order || col >= p->order )
		return 0;

	if( !SQRMATRIX_CreateMatrix( minor, p->order-1 ))
		return 0;

	a = b = 0;

	for( i = 0; i < p->order; i++ )
	{
		if( i != row )
		{
			b = 0;
			for( j = 0; j < p->order; j++ )
			{
				if( j != col )
				{
					minor->array[a][b] = p->array[i][j];
					b++;		// Increase column-count of minor
				}
			}
			a++;			// Increase row-count of minor
		}
	}

	return 1;
}

/* Calculate the determinant recursively.
	The recursive definition is :
		det( m ) = Summation( i = 0 to order ) [ (-1)^i * m[0][i] * det( minor( m[0][i] ))]
*/
int SQRMATRIX_CalcDeterminant( SQRMATRIX *p )
{
	int i, result = 0;
	SQRMATRIX minor;

 	if( p->order < 1 )
 	{
 		printf("CalcDeterminant( ) : Invalid matrix.");
 		return 0;
 	}

 		// The 'stopping' condition
 	if( p->order == 1 )
 		return p->array[0][0];

 	for( i = 0; i < p->order; i++ )
 	{
 		if( !SQRMATRIX_CalcMinor( p, &minor, 0, i ))
 		{
 			printf("CalcDeterminant( ) : Memory allocation failed.");
 			return 0;
 		}

 		result += ( pow( -1, i ) * p->array[0][i] * SQRMATRIX_CalcDeterminant(&minor ));

 		SQRMATRIX_DestroyMatrix( &minor );
 	}

 	return result;
}
		// Release allocated memory
void SQRMATRIX_DestroyMatrix( SQRMATRIX *p )
{
	int i;

	if( p->order < 1 )
		return;

	for( i = 0; i < p->order; i++ )
		free( p->array[i] );		// free each columns

	free( p->array );		// free each row
	p->order = 0;
}
