def fact(x):
  if(x<0):
    return "invalid number"  
  if(x==0):
    return 1
  if(x==1):
    return x
  else: 
     return x*fact(x-1)
  print(x)
z=fact(-2)
print(z)

