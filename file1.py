fileptr = open("BinarySearch.java","r");   
  
#stores all the data of the file into the variable content  
content = fileptr.readline();   
  
# prints the type of the data stored in the file  
print(type(content))   
  
#prints the content of the file  
print(content)   
  
#closes the opened file  
fileptr.close()  