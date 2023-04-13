def calculateAddition(n):  
  return n+n  
  
numbers = (1, 2, 3, 4)  
result = map(calculateAddition, numbers)  
print(result)  
  
# converting map object to set  
numbersAddition = list(result)  
print(numbersAddition)  
