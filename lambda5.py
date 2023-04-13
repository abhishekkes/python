mx=lambda a,d,i:a+i*d
n=int(input("enter the number of terms"))
a=int(input("enter the 1st term"))
d=int(input("enter the common difference"))
for i in range(n):
	print(mx(a,d,i))