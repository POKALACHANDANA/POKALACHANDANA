try:
	a=input("Enter value of a :")
	b=input("Enter value of b:")
	div=float(a)/float(b)
	print("The result=",div)
except ValueError:
	print("Enter either interger or float")
