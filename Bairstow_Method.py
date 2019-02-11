from sympy import *
import sys
import numpy as np
sys.displayhook = pprint
init_printing()
print('\n\nInitial Setup Complete')

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
bairstow(expression,f)