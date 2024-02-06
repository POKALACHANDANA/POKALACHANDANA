a=[1,2]
b=[3,4]
sum=0
for i in range(len(a)):
	if(type(a[i])!=type("a") and type(b[i])!=type("b")):
		p=a[i]*b[i]
		sum=sum+p
	else:
		print("not possible")
print("the dot product =%d"%sum)
	
