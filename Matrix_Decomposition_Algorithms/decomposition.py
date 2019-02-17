import numpy as np

def doolittle(A,n):
	print("\nUsing Doolittle Method for LU Decomposition\n")
	L=np.identity(n)
	U=np.zeros((n,n))
	for i in range(n):
		for k in range(n):
			if i<=k:
				U[i,k] = A[i,k] - sum([L[i,j]*U[j,k] for j in range(0,i)])
			else:
				L[i,k] = (  A[i,k] - sum([L[i,j]*U[j,k] for j in range(0,i)])  )/U[k,k]
	print("A = LU, where - \n")
	print("Matrix L = \n",L)
	print("Matrix U = \n",U)

def crout(A,n):
	print("\nUsing Crout Method for LU Decomposition\n")
	L=np.zeros((n,n))
	U=np.identity(n)
	for i in range(n):
		for k in range(n):
			if i<k:
				U[i,k] = (A[i,k] - sum([L[i,j]*U[j,k] for j in range(0,i)]))/L[i,i]
			else:
				L[i,k] = A[i,k] - sum([L[i,j]*U[j,k] for j in range(0,k)])
	print("A = LU, where - \n")
	print("Matrix L = \n",L)
	print("Matrix U = \n",U)

def cholesky(A,n):
	print("\nUsing Cholesky Method for (L)(L.T) Decomposition\n")
	L=np.zeros((n,n))
	for i in range(n):
		for k in range(0,i+1):
			if i==k:
				L[i,i] = (A[i,i] - sum( [ L[i,j]**2 for j in range(0,i) ] ))**0.5
			elif i>k:
				L[i,k] = (A[k,i] - sum ( [ L[k,j]*L[i,j] for j in range(0,k) ] ) )/L[k,k]			
	print("A = (L)(L.T), where - \n")
	print("Matrix L = \n",L)
	print("Matrix L.T = \n",L.T)

#Take matrix size as input
n=int(input("Enter n for matrix size nxn :  "))
#initialise nxn matrix with zeroes
A=np.zeros((n,n))
print("Input each row at a time, with each element separated by a space : \n")
for i in range(n):
   A[i]=input().split(" ")
print("Matrix A = \n",A)
ch = int(input("""
\n\n
Enter choice for LU Decomposition: 
	1. Doolittle Method
	2. Crout Method
	3. Cholesky Decomposition
\n\n"""))
if (ch==1):
	doolittle(A,n)
elif (ch==2):
	crout(A,n)
elif(ch==3):
	cholesky(A,n)