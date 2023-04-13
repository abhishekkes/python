list1=[1,2,3,4,5,6]
newlist=list(map(lambda y:y*3,(list(filter(lambda x: x%2==0,list1)))))
print(newlist)