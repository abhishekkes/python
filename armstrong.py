x=153
y=x
num=0
while(x>0):
 z=x%10
 num=num+z**3
 x=x//10
if(y==num):
 print(y,"is armstrong number")
