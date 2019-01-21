from __future__ import division
from IPython.display import display, Math, Latex
from sympy import *
import numpy as np
init_printing()
print('\n\nInitial Setup Complete')

def guess_initial_estimates(f):
	found_ab = 0
	rnge=1
	nm_trials = rnge*500
	print "Guessing Initial Estimates a,b"
	while(found_ab==0):
		print "Trying "+ str(nm_trials)+ " random numbers from uniform continuous distribution in range [-" +str(rnge)+"," +str(rnge)+"]"
		trial_points = np.random.uniform(low=-1*rnge, high=rnge, size=nm_trials)
		#print trial_points
		evaluations = f(trial_points)		
		evaluations = np.array([float((N(x))) for x in evaluations])
		#print evaluations
		prob_pos = np.argmax(evaluations)
		prob_neg = np.argmin(evaluations)
		if evaluations[prob_pos]>0 and evaluations[prob_neg]<0 :
			a,b = min(trial_points[prob_pos],trial_points[prob_neg]),max(trial_points[prob_pos],trial_points[prob_neg])
			print "	FOUND"
			found_ab=1
		else :
			print "	failed"
			rnge = rnge*5
			nm_trials = rnge*100
	return (a,b)

def take_good_a_b(f):
	#Say a and b are "good" if f(a)*f(b)<0
	got=0
	while(got==0):
		a, b = map(float, raw_input("Enter a,b : ").strip().split())
		if (N(f(a))*N(f(b))<0):
			got=1
		elif (N(f(a))*N(f(b))>0):
			print "Try Again : Your approximations a,b give f(a)*f(b)>0"
	return (a,b)

def bisection_method(f):
	ch = input("Enter 1 if you will enter Initial Estimates a,b.\nEnter 2 for program to guess initial estimates.\n")
	if ch==1:
		a,b=take_good_a_b(f)
	else:
		a,b = guess_initial_estimates(f)

	err = float(input("Enter error tolerance : "))
	print "Starting Bisection Process"
	print "	a , b = ",a,",",b
	print "	f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0

	exact_root_found =0
	root = 0
	while (float(abs(b-a)) > err):
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		m = (b+a)/2.0
		m_val = N(f(m))
		if m_val==0:
			print "Exact Root found"
			root = m
			exact_root_found =1
			break
		elif m_val*N(f(a))<0:
			a,b = min(m,a),max(m,a)
		else:
			a,b=  min(m,b),max(m,b)
		print "	a , b = ",a,",",b
		print "	f(a) , f(b) = ",f(a),",",f(b)
		
	if exact_root_found==0:
		print "Root Approximated within error range."
		root = (a+b)/2.0
	print "Number of Iterations = ",iter_count
	print "	Root = ",root
	print "	f(Root) = ",f(root)

def secant_method(f):
	a, b = map(float, raw_input("Enter 2 approximations a,b : ").split())
	err = float(input("Enter error tolerance : "))
	print "Starting Secant Method"
	print "	a , b = ",a,",",b
	print "	f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root = 0
	a,b = min(a,b) , max(a,b)
	while (float(abs(b-a)) > err):
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		
		if N(f(b)-f(a))==0:
			print "	Not Converging"
			not_converging = 1
			break
		x_ = b - ((b-a)/(f(b)-f(a)))*f(b)
		
		x_val = f(x_)
		if N(x_val)==0:
			print "	Exact Root found"
			root = x_
			exact_root_found =1
			break
		else:
			a,b = b , x_
		print "	a , b = ",a,",",b
		print "	f(a) , f(b) = ",f(a),",",x_val

	if not_converging == 0 and exact_root_found==0:
		print "Root Approximated within error range."
		root = b
	if not_converging ==0:
		print "Number of Iterations = ",iter_count
		print "	Root = ",root
		print "	f(Root) = ",f(root)

def regula_falsi(f):
	ch = input("Enter 1 if you will enter Initial Estimates a,b.\nEnter 2 for program to guess initial estimates.\n")
	if ch==1:
		a,b = take_good_a_b(f)
	else:
		a,b = guess_initial_estimates(f)

	err = float(input("Enter error tolerance : "))
	print "Starting Regula-Falsi Method"
	print "	a , b = ",a,",",b
	print "	f(a) , f(b) = ",f(a),",",f(b)
	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root = 0

	a,b = min(a,b) , max(a,b)
	x_prev = a
	x_ = b
	while (float(abs(x_prev-x_)) > err):
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		
		if N(f(b)-f(a))==0:
			print "	Not Converging"
			not_converging = 1
			break
		x_prev = x_
		x_ = (b - ((b-a)/(f(b)-f(a)))*f(b))
		
		x_val = f(x_)
		if x_val==0:
			print "	Exact Root found"
			root = x_
			exact_root_found =1
			break
		else:
			if x_val*N(f(a))<0:
				a,b = a,x_
			if x_val*N(f(b))<0:
				a,b = x_,b
		print "	a , b = ",a,",",b
		print "	f(a) , f(b) = ",f(a),",",f(b)

	if not_converging == 0 and exact_root_found==0:
		print "Root Approximated within error range."
		root = x_
	if not_converging ==0:
		print "Number of Iterations = ",iter_count
		print "	Root = ",root
		print "	f(Root) = ",f(root)

def newton_raphson(expression , f):
	#see the dfferentiation of the function
	print "Starting Newton-Raphson Method"
	#print "f(x) = ",expression
	f_dash = diff(expression,x)
	#print "df(x)/dx = " , f_dash
	a = float(input("Enter initial approximation: "))
	err = float(input("Enter error tolerance : "))
	print "	x0 = ",a
	print "	f(x0) = ",f(a)
	iter_count = 0
	exact_root_found =0
	not_converging = 0
	root=a
	xk=root
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
			root = (xk - fk/fk_dash)
			if N(f(root))==0:
				exact_root_found=1
				print "Exact Root Found"
				break
			elif abs(N(root-xk)) < float(err):
				break
		
		print "	x"+str(iter_count)+" = ",xk
		print "	f(x"+str(iter_count)+") = ",f(xk)

	if not_converging == 0 and exact_root_found==0:
		print "Root Approximated within error range."
	if not_converging ==0:
		print "Number of Iterations = ",iter_count
		print "	Root = ",root
		print "	f(Root) = ",f(root)

#Syntax Constraints
print("""		
	Syntax Constraints for entering function - 

	x**y means x raised to the power of y
	Function must be algebraic combination of one or more of - 

	p(x)      Polynomials
	exp(x)    Mathematical constant e (2.71828...) raised to power x
	pi        Mathematical constant 3.14159...
	log(x)    Natural Logarithm
	acos(x)   Arc cosine of x
	asin(x)   Arc sine of x
	atan(x)   Arc tangent of x
	cos(x)    Cosine of x
	sin(x)    Sine of x
	tan(x)    Tangent of x
	acosh(x)  Inverse hyperbolic cosine of x
	asinh(x)  Inverse hyperbolic sine of x
	atanh(x)  Inverse hyperbolic tangent of x
	cosh(x)   Hyperbolic cosine of x
	sinh(x)   Hyperbolic cosine of x
	tanh(x)   Hyperbolic tangent of x	
		
		""")
#example s is given
#s = '-2*((-x+1/x)/(x*(x-1/x)**2)-1/(x*(x-1/x)))'
x = Symbol('x')
s=raw_input("Enter a function :  ").strip()
expression=sympify(s)
#will lambdify expression for fast parrallel multipoint computation 
f = lambdify(x, expression, "numpy")
#print("Verify f(0.9)")
#print N(f(0.9))

try_again=1
while(try_again==1):
	print "\nf(x) = ",expression
	f_dash = diff(expression,x)
	print "df(x)/dx = " , f_dash
	print """Select Index of Iterative Method:
		 1. Bisection Method
		 2. Secant Method
		 3. Regula-Falsi Method
		 4. Newton-Raphson Method
				 """
	choice_of_method = input()
	if (choice_of_method==1):		bisection_method(f)
	elif (choice_of_method==2):		secant_method(f)
	elif (choice_of_method==3):		regula_falsi(f)
	elif (choice_of_method==4):		newton_raphson(expression,f)
	try_again=0
	k = (raw_input("Try another method? [Y/N] : ")).strip()
	try_again = 1 if (k=='y' or k=='Y') else 0