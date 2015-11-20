#ifndef __DETERMINANT_H__
#define __DETERMINANT_H__
// A square matrix struct
typedef struct
{
	int order;
	int **array;

} SQRMATRIX;

		// Function declarations
int SQRMATRIX_CreateMatrix( SQRMATRIX *p, int order );
void SQRMATRIX_DisplayMatrix( SQRMATRIX *p );
void SQRMATRIX_InputMatrix( SQRMATRIX *p );
int SQRMATRIX_CalcMinor( SQRMATRIX *p, SQRMATRIX *minor, int row, int col );
int SQRMATRIX_CalcDeterminant( SQRMATRIX *p );
void SQRMATRIX_DestroyMatrix( SQRMATRIX *p );


#endif // __DETERMINANT_H__
