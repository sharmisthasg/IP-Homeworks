# MEGHNA GUPTA - 2016056
# SHARMISHTHA GUPTA - 2016193


def swapRows(A,row1,row2):
	
	""" 
	the matrix function, swapRows(A,row1,row2)​, that performs a swap between two rows of a given
matrix.
The function takes 3 arguments:
 A represents the matrix
 row1 and row2 are indices of the rows to swap. The possible values for the arguments row1 and
row2 are 0, ..., nrows - 1, where nrows in number of rows in A	
	"""

	temp = A[row2]
	A[row2] = A[row1]
	A[row1] = temp
	return A



def swapCol(A,col1,col2):
	"""
	This matrix function has just been defined for convenience to swap two columNs of a matrix.
	"""



def Row_Transformation(A,x,row1,row2,val = 1):
	"""
	 a matrix function, Row_Transformation(A, x, row1, row2 )​, that performs row transformation on
matrix A by transforming as
row2 → row2 + x * row1
	"""
	i = 0

	while i < len(A[row1]):
		A[row2][i] = (A[row2][i] + x*A[row1][i]) / val
		i = i + 1
	return A


def MatrixRank(A):
	"""
	This function returns the rank of a matrix.
	"""
	no_of_col = len(A[0])
	no_of_rows = len(A)
	temp = min(no_of_rows,no_of_col)
	i = 0
	for i in range(temp):
		if A[i][i] != 0:
			for j in range(0,no_of_rows):
				if j != i:
					x = A[j][i]/A[i][i]
					A = Row_Transformation(A,x,j,i)

		else:
			flag = 0

			for j in range(i+1,no_of_rows):

				
				if A[j][i] != 0:
					swapRows(A,i,j)
					flag = 1
					break

			if flag == 0:
				temp = temp - 1
				for k in range(no_of_rows):
					swapCol(A,i,temp - 1)
			i = i - 1


	z = 0
	rank = 0 
	counter = 0

	for z in range(no_of_rows):
		for y in range(no_of_col):
			if A[z][y] != 0:
				counter = counter + 1
		if counter > 0:
			rank = rank + 1
		counter = 0
	return rank 


