import numpy as np

#Take matrix size as input
n=int(input("Enter n for matrix size nxn :  "))
#initialise nxn matrix with zeroes
A=np.zeros((n,n))
print("Input each row at a time, with each element separated by a space : \n")
for i in range(n):
   A[i]=input().split(" ")

print("Matrix A = \n",A)
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