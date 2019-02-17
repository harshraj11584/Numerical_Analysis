import numpy as np

def gauss_seidel(A,b,x0,err,n):
	iter_count = 0
	L = np.zeros((n,n))
	U = np.zeros((n,n))
	D = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i>j:
				L[i,j] = A[i,j]
			elif i==j:
				D[i,j] = A[i,j]
			else:
				U[i,j] = A[i,j]
	x1=x0
	x0 = np.reshape(np.zeros((n,1)),(n,1))
	del_x = x1-x0
	LpU = L+U
	while (np.linalg.norm(del_x) >err):
		x0 = x1
		x1 = -np.matmul((np.matmul(np.linalg.inv(D+L),U)),x0)+np.matmul(np.linalg.inv(D+L),b)
		iter_count=iter_count+1
		print ("Iteration No. ", iter_count, ": ")
		print ("x= ", x1.T)
		del_x = x1-x0
	print ("\n\nFound.\n x = ", x1.T)


def gauss_jacobi(A,b,x0,err,n):
	iter_count = 0
	L = np.zeros((n,n))
	U = np.zeros((n,n))
	D = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i>j:
				L[i,j] = A[i,j]
			elif i==j:
				D[i,j] = A[i,j]
			else:
				U[i,j] = A[i,j]
	x1=x0
	x0 = np.reshape(np.zeros((n,1)),(n,1))
	del_x = x1-x0
	LpU = L+U
	while (np.linalg.norm(del_x) >err):
		x0 = x1
		x1 = np.matmul((-1*np.matmul(np.linalg.inv(D),L+U)),x0)+np.matmul(np.linalg.inv(D),b)
		iter_count=iter_count+1
		print ("Iteration No. ", iter_count, ": ")
		print ("x= ", x1.T)
		del_x = x1-x0
	print ("\n\nFound.\n x = ", x1.T)

print("Iteratively Solving Ax=b")
#Take matrix size as input
n=int(input("Enter n for matrix A of size nxn :  "))
#initialise nxn matrix with zeroes
A=np.zeros((n,n))
print("Input each row at a time, with each element separated by a space : \n")
for i in range(n):
   A[i]=input().strip().split(" ")
   A[i]=[float(x) for x in A[i]]

print("Input vector b, each coordinate separated by space : ")
b = input().strip().split(" ")
b = [float(x) for x in b]
b = np.reshape(b,(n,1))

print("Input Intial guess vector x for Ax=b: ")
x0 = input().strip().split(" ")
x0 = [float(x) for x in x0]
x0 = np.reshape(x0,(n,1))
print("Guess x0 = \n",x0)
err = float(input("Enter max error in norm of x: "))

#sample input
# n =2
# A = np.matrix('2 1;5 7')
# b = np.matrix('11;13')
# x0 = np.matrix('1;1')
# err = 0.00001

print("Matrix A = \n",A)
print ("Vector b = \n",b)

print ("""Select Index of Solving Method:
		 1. Gauss-Jacobi Method
		 2. Gauss-Seidel Method
				 """)
choice_of_method = int(input())
if (choice_of_method==1):		gauss_jacobi(A,b,x0,err,n)
elif (choice_of_method==2):		gauss_seidel(A,b,x0,err,n)
