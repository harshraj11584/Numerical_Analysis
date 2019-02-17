from sympy import *
import sys
import numpy as np
sys.displayhook = pprint
init_printing()
print('\n\nInitial Setup Complete')
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
	iter_count = 0
	while(abs(N(new_root-prev_root))>=err):
		iter_count = iter_count + 1
		print "Iteration No. ", iter_count, ": "
		tmp = new_root
		new_root = new_root-float(N(b_n.subs([(x,1),(p,new_root)])))/float(N((c_n_minus_1.subs([(x,1),(p,new_root)]))))
		#print b_n.degree_list()
		#this = float(N(b_n.subs([(x,1),(p,new_root)])))
		#print this
		#print type(this)
		prev_root = tmp
		print "	x"+str(iter_count)+" = ",new_root
		print "	f(x"+str(iter_count)+") = ",f(new_root)

	print "\n\nRoot Approximated within error range."
	print "Number of Iterations = ",iter_count
	print "	Root = ",new_root
	print "	f(Root) = ",f(new_root)



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
x = Symbol('x')
s=raw_input("Enter a function :  ").strip()
expression=sympify(s)
#will lambdify expression for fast parrallel multipoint computation 
f = lambdify(x, expression, "numpy")
#print("Verify f(0.9)")
#print N(f(0.9))
birge_vieta(expression,f)