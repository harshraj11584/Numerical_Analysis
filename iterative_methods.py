#MA17BTECH11003
# from __future__ import division
# from IPython.display import display, Math, Latex
from sympy import *
import sys
import numpy as np
sys.displayhook = pprint
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


def birge_vieta(expression,f):
	print "Starting Birge Vieta Method"
	print "\nPn(x) = \n" 
	pprint(expression)	
	Pn = Poly(expression,x)
	a = []*degree(Pn, gen=x)
	a = Pn.all_coeffs()
	print "\na_0, a_1, a_2, ... a_"+str(degree(Pn,gen=x))+" are: ",a,"\n"
	p = Symbol('p')
	Qn, R = div(Pn,(x-p))
	print "\nb_n=\n\n",
	pprint(R.as_expr())
	b_n = R
	c_n_minus_1 = diff(b_n,p)

	p0 = float(input("\nEnter initial approximation p0: "))
	err = float(input("Enter error tolerance : "))
	prev_root = 0 ; new_root = p0
	iter_count = 0 ; not_converging = 0
	while(abs(N(new_root-prev_root))>err):
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		tmp = new_root
		if (float(N((c_n_minus_1.subs([(x,1),(p,new_root)]))))==0):
			print ("Not Converging\n")
			not_converging = 1
			break;
		new_root = new_root-float(N(b_n.subs([(x,1),(p,new_root)])))/float(N((c_n_minus_1.subs([(x,1),(p,new_root)]))))
		#print b_n.degree_list()
		#this = float(N(b_n.subs([(x,1),(p,new_root)])))
		#print this
		#print type(this)
		prev_root = tmp
		print "	x"+str(iter_count)+" = ",new_root
		print "	f(x"+str(iter_count)+") = ",f(new_root)

	if (not_converging==0):
		print "\n\nRoot Approximated within error range."
		print "Number of Iterations = ",iter_count
		print "	Root = ",new_root
		print "	f(Root) = ",f(new_root)

def bairstow(expression,f):
	print "Starting Bairstow's Method"
	print "\nPn(x) = " 
	pprint(expression)
	Pn = Poly(expression,x)	
	p = Symbol('p')
	q = Symbol('q')
	quad_div = Poly(sympify('x**2 + p*x+q'),x)
	print "Suppose this quadratic polynomial divides Pn(x) : "
	pprint (sympify('x**2 + p*x+q'))
	Qn, Rem = div(Pn,quad_div)
	p0,q0 = 0,0
	p1,q1 = map(float, raw_input("\nEnter initial guess p,q: ").split())
	err = float(input("Enter error tolerance : "))
	print("Remainder is : ",Rem)
	R,S = div(Rem,x)
	print("R=",R,"S=",S)
	Rp = diff(R,p)
	Rq = diff(R,q)
	Sp = diff(S,p)
	Sq = diff(S,q)	
	del_p = - (R*Sq - S*Rq)/(Rp*Sq - Rq*Sp)
	del_q = - (Rp*S - Sp*R)/(Rp*Sq - Rq*Sp)
	iter_count = 0
	while abs(p1-p0)>err or abs(q1-q0)>err : 
		pt,qt = p1,q1
		p_inc =  float(N(del_p.subs([(x,1),(p,p1),(q,q1)])))
		q_inc =  float(N(del_q.subs([(x,1),(p,p1),(q,q1)])))
		p1 = p1 + p_inc
		q1 = q1 + q_inc
		p0,q0 = pt,qt
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		print "	p"+str(iter_count)+" = ",p1
		print "	q"+str(iter_count)+" = ",q1
	print "\n\nFound.\nQuadratic Equation that divides Pn(x) is \n"
	quad_div = sympify("x**2+"+str(p1)+"*x+"+str(q1))
	pprint(quad_div)
	print "\n\nRoots are ",solve(quad_div, x)


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
#s="(7/2)*x**3 - x**9 +1"
#s="6*x**5+11*x**4 -33*x**3-33*x**2 + 11*x+6"
x = Symbol('x')
s=raw_input("Enter a function :  ").strip()
expression=sympify(s)

#will lambdify expression for fast parrallel multipoint computation 
f = lambdify(x, expression, "numpy")
#print("Verify f(0.9)")
#print N(f(0.9))

try_again=1
while(try_again==1):
	print("\nf(x) = \n")
	pprint(expression)
	f_dash = diff(expression,x)
	print "\ndf(x)/dx = \n"
	pprint(f_dash)
	print """Select Index of Iterative Method:
		 1. Bisection Method
		 2. Secant Method
		 3. Regula-Falsi Method
		 4. Newton-Raphson Method
		 5. Birge-Vieta Method
		 6. Bairstow's Method
				 """
	choice_of_method = input()
	if (choice_of_method==1):		bisection_method(f)
	elif (choice_of_method==2):		secant_method(f)
	elif (choice_of_method==3):		regula_falsi(f)
	elif (choice_of_method==4):		newton_raphson(expression,f)
	elif (choice_of_method==5):		birge_vieta(expression,f)
	elif (choice_of_method==6): 	bairstow(expression,f)
	try_again=0
	k = (raw_input("Try another method? [Y/N] : ")).strip()
	try_again = 1 if (k=='y' or k=='Y') else 0