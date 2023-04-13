n=int(input("Enter the pattern row"))
for i in range(n):
 for k in range (n-i-1):
   print(" ",end="")
 for j in range (0,i+1):
   print("*",end="")
 print()  