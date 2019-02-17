# MA5060_Numerical_Analysis

Numerical Techniques, All Implemented from scratch in Python

## 1. Root Finding Algorithms for f(x)=0 :  
  1. Bisection Method
  2. Secant Method
  3. Regula-Falsi Method
  4. Newton-Raphson Method
  5. Birge-Vieta Method
  6. Bairstow's Method

 - Functions can be any algebraic combinations of polynomials Pn(x), exp(x), pi, log2(x),log10(x), acos(x),	asin(x) ,atan(x) , cos(x) ,sin(x), tan(x), acosh(x),asinh(x),atanh(x),cosh(x), sinh(x), tanh(x) ,gamma(x), lgamma(x)  
 - All algorithms have independent implementations.
 - The iterative_methods.py file has all algorithms together, and can compare performance and convergence of all these methods. 
 - Also implemented pretty printing for all functions, so functions can be printed in their mathematical notational form within the terminal.
### Dependencies: Python 2.7, Numpy 1.16.1, Sympy 1.3

## 2. Matrix Decomposition Algorithms :   
  1.  LU Decomposition   
    a) DooLittle Method, L[i,i]=1, Implemented in O(nxn)   
    b) Crout's Method, U[i,i]=1, Implemented in O(nxn)   
  2.  L(L.T) Decompostion   
    a) Cholesky's Method
 - All algorithms have independent implementations.
 - The decomposition.py file has all algorithms together, and can compare performance and convergence of all these methods.
  ### Dependencies: Python 3.6.7, Numpy 1.16.1
  
## 3. Matrix Equation Solvers for Ax=b :
  1. Gauss-Jacobi Method
  2. Gauss-Seidel Method
 - All algorithms have independent implementations.
 - The solving_matrix_equations.py file has all algorithms together, and can compare performance and convergence of methods.
  ### Dependencies: Python 3.6.7, Numpy 1.16.1
  
## 4. Matrix Inversion
  - O(n^3) Algorithm.
  - Prints the inverse of the matrix if it is invertible, 'INVALID' otherwise. Also handles NaN exceptions.
  ### Dependencies: E
