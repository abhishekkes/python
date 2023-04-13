a=b=c=0
for x in "aerop567lane123":
  if(x=='a' or x=='i' or x=='e' or x=='o' or x=='u'):   
   print(x)
   c=c+1
  elif (x>='0' and x<='9'):
   print(x)
   b=b+1
  else:
   a=a+1  
print(c,' ',a,' ',b)

	
