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

#Take matrix size as input
n=int(input("Enter n for matrix size nxn :  "))
#initialise nxn matrix with zeroes
A=np.zeros((n,n))
print("Input each row at a time, with each element separated by a space : \n")
for i in range(n):
   A[i]=input().split(" ")
print("Matrix A = \n",A)
ch = int(input("\n\nEnter choice for LU Decomposition: \n 1. Doolittle Method\n 2. Crout Method\n\n"))
if (ch==1):
	doolittle(A,n)
elif (ch==2):
	crout(A,n)