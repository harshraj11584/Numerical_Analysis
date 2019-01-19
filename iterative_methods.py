from __future__ import division
from IPython.display import display, Math, Latex
from sympy import *
import numpy as np
init_printing()
print('Initial Setup Complete')



def bisection_method(f):
	print "Enter 1 if you will enter Initial Estimates a,b."
	print "Enter 2 for program to guess initial estimates."
	ch = input()
	if ch==1:
	    got=0
	    while(got==0):
	        a, b = map(int, raw_input("Enter a,b : ").split())
	        if (f(a)*f(b)<0):
	            got=1
	        elif (f(a)*f(b)>0):
	            print "Try Again : Your approximations a,b give f(a)*f(b)>0"
	else:
	    found_ab = 0
	    rnge = 1
	    nm_trials = rnge*100
	    print "Guessing Initial Estimates a,b"
	    while(found_ab==0):
	        print "Trying "+ str(nm_trials)+ " random numbers from uniform continuous distribution in range [-" +str(rnge)+"," +str(rnge)+"]"
	        trial_points = np.random.uniform(low=-1*rnge, high=rnge, size=nm_trials)
	        #print trial_points
	        evaluations = f(trial_points)
	        #print evaluations
	        prob_pos = np.argmax(evaluations)
	        prob_neg = np.argmin(evaluations)
	        if evaluations[prob_pos]>0 and evaluations[prob_neg]<0 :
	            a,b = min(trial_points[prob_pos],trial_points[prob_neg]),max(trial_points[prob_pos],trial_points[prob_neg])
	            print "    FOUND"
	            found_ab=1
	        else :
	            print "    failed"
	            rnge = rnge*5
	            nm_trials = rnge*100

	err = input("Enter error tolerance : ")
	print "Starting Bisection Process"
	print "    a , b = ",a,",",b
	print "    f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0

	exact_root_found =0
	root = 0
	while (abs(b-a) > err):
	    iter_count = iter_count + 1
	    print "Iteration No. ", iter_count, ": "
	    m = (b+a)/2.0
	    m_val = f(m)
	    if m_val==0:
	        print "Exact Root found"
	        root = m
	        exact_root_found =1
	        break
	    elif m_val*f(a)<0:
	        a,b = min(m,a),max(m,a)
	    else:
	        a,b=  min(m,b),max(m,b)
	    print "    a , b = ",a,",",b
	    print "    f(a) , f(b) = ",f(a),",",f(b)
	    
	if exact_root_found==0:
	    print "Root Approximated within error range."
	    root = (a+b)/2.0
	print "Number of Iterations = ",iter_count
	print "    Root = ",root
	print "    f(Root) = ",f(root)





def secant_method(f):
	a, b = map(int, raw_input("Enter 2 approximations a,b : ").split())
	err = input("Enter error tolerance : ")
	print "Starting Secant Method"
	print "    a , b = ",a,",",b
	print "    f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root = 0
	a,b = min(a,b) , max(a,b)
	while (abs(b-a) > err):
	    iter_count = iter_count + 1
	    print "Iteration No. ", iter_count, ": "
	    
	    if f(b)-f(a)==0:
	        print "    Not Converging"
	        not_converging = 1
	        break
	    x_ = b - ((b-a)/(f(b)-f(a)))*f(b)
	    
	    x_val = f(x_)
	    if x_val==0:
	        print "    Exact Root found"
	        root = x_
	        exact_root_found =1
	        break
	    else:
	        a,b = b , x_
	    print "    a , b = ",a,",",b
	    print "    f(a) , f(b) = ",f(a),",",x_val

	if not_converging == 0 and exact_root_found==0:
	    print "Root Approximated within error range."
	    root = b
	if not_converging ==0:
	    print "Number of Iterations = ",iter_count
	    print "    Root = ",root
	    print "    f(Root) = ",f(root)



def regula_falsi(f):
	print "Enter 1 if you will enter Initial Estimates a,b."
	print "Enter 2 for program to guess initial estimates."
	ch = input()
	if ch==1:
	    got=0
	    while(got==0):
	        a, b = map(int, raw_input("Enter a,b : ").split())
	        if (f(a)*f(b)<0):
	            got=1
	        elif (f(a)*f(b)>0):
	            print "Try Again : Your approximations a,b give f(a)*f(b)>0"
	else:
	    found_ab = 0
	    rnge = 1
	    nm_trials = rnge*100
	    print "Guessing Initial Estimates a,b"
	    while(found_ab==0):
	        print "Trying "+ str(nm_trials)+ " random numbers from uniform continuous distribution in range [-" +str(rnge)+"," +str(rnge)+"]"
	        trial_points = np.random.uniform(low=-1*rnge, high=rnge, size=nm_trials)
	        #print trial_points
	        evaluations = f(trial_points)
	        #print evaluations
	        prob_pos = np.argmax(evaluations)
	        prob_neg = np.argmin(evaluations)
	        if evaluations[prob_pos]>0 and evaluations[prob_neg]<0 :
	            a,b = min(trial_points[prob_pos],trial_points[prob_neg]),max(trial_points[prob_pos],trial_points[prob_neg])
	            print "    FOUND"
	            found_ab=1
	        else :
	            print "    failed"
	            rnge = rnge*5
	            nm_trials = rnge*100

	err = input("Enter error tolerance : ")
	print "Starting Regula-Falsi Method"
	print "    a , b = ",a,",",b
	print "    f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root = 0
	a,b = min(a,b) , max(a,b)
	while (abs(b-a) > err):
	    iter_count = iter_count + 1
	    print "Iteration No. ", iter_count, ": "
	    
	    if f(b)-f(a)==0:
	        print "    Not Converging"
	        not_converging = 1
	        break
	    x_ = b - ((b-a)/(f(b)-f(a)))*f(b)
	    
	    x_val = f(x_)
	    if x_val==0:
	        print "    Exact Root found"
	        root = x_
	        exact_root_found =1
	        break
	    else:
	        if x_val*f(a)<0:
	            a,b = a,x_
	        if x_val*f(b)<0:
	            a,b = x_,b
	    print "    a , b = ",a,",",b
	    print "    f(a) , f(b) = ",f(a),",",f(b)

	if not_converging == 0 and exact_root_found==0:
	    print "Root Approximated within error range."
	    root = b
	if not_converging ==0:
	    print "Number of Iterations = ",iter_count
	    print "    Root = ",root
	    print "    f(Root) = ",f(root)


def newton_raphson(expression , f):
	#see the dfferentiation of the function
	print "Starting Newton-Raphson Method"
	f_dash = diff(expression,x)
	print "df(x)/dx = " , f_dash
	a = input("Enter initial approximation: ")
	err = input("Enter error tolerance : ")
	print "    x0 = ",a
	print "    f(x0) = ",f(a)

	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root=a

	while (True):
	    iter_count = iter_count + 1
	    print "Iteration No. ", iter_count, ": "
	    xk=root
	    fk = f(xk)    
	    #this is the expression for f_dash
	    
	    fk_dash= (lambdify(x , f_dash , "numpy"))(xk)
	    
	    if fk_dash ==0:
	        not_converging =1
	        print "Not Converging"
	        break;
	    else:
	        root = xk - fk/fk_dash
	        if f(root)==0:
	            exact_root_found=1
	            print "Exact Root Found"
	            break;
	        elif abs(root-xk)<err:
	            break;  
	    
	    print "    x"+str(iter_count)+" = ",xk
	    print "    f(x"+str(iter_count)+") = ",f(xk)

	if not_converging == 0 and exact_root_found==0:
	    print "Root Approximated within error range."
	if not_converging ==0:
	    print "Number of Iterations = ",iter_count
	    print "    Root = ",root
	    print "    f(Root) = ",f(root)



x = Symbol('x')
#Syntax Constraints
print("""        
        Syntax Constraints for entering function - 
        
        x**y means x raised to the power of y
        
        Function must be algebraic combination of one or more of - 
        
        p(x)        Polynomials and their algebraic combinations
        exp(x)      Returns e**x
        log2(x)     Returns the base-2 logarithm of x
        log10(x)    Returns the base-10 logarithm of x
        acos(x)     Returns the arc cosine of x
        asin(x)     Returns the arc sine of x
        atan(x)     Returns the arc tangent of x
        cos(x)      Returns the cosine of x
        sin(x)      Returns the sine of x
        tan(x)      Returns the tangent of x
        acosh(x)    Returns the inverse hyperbolic cosine of x
        asinh(x)    Returns the inverse hyperbolic sine of x
        atanh(x)    Returns the inverse hyperbolic tangent of x
        cosh(x)     Returns the hyperbolic cosine of x
        sinh(x)     Returns the hyperbolic cosine of x
        tanh(x)     Returns the hyperbolic tangent of x
        gamma(x)    Returns the Gamma function at x
        lgamma(x)   Returns the natural logarithm of the absolute value of the Gamma function at x
        pi          Mathematical constant 3.14159...
        e           Mathematical constant e (2.71828...)
         
        
        """)
#example s is given
#s = '-2*((-x+1/x)/(x*(x-1/x)**2)-1/(x*(x-1/x)))'
s=raw_input("Enter a function :  ").strip()
expression=sympify(s)
print "This is the function : "
print expression

#will lambdify expression for fast parrallel computation at random points
f = lambdify(x, expression, "numpy")
print("Verify f(0.9)")
print f(0.9)

print """Select Index of Iterative Method:
	 1. Bisection Method
	 2. Secant Method
	 3. Regula-Falsi Method
	 4. Newton-Raphson Method
			 """

choice_of_method = input()
if (choice_of_method==1):
	bisection_method(f)
elif (choice_of_method==2):
	secant_method(f)
elif (choice_of_method==3):
	regula_falsi(f)
elif (choice_of_method==4):
	newton_raphson(expression,f)