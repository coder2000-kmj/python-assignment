#to count the number of Characters in a given string and hence to display the characters of string in reverse order. 
def reverse(s):
    str=""
    for i in s:
        str = i + str
    return str


#main
s = "Welcome To SDMIT"  
count=0
for i in s:
    count=count+1
print(count)
print ("The original string  is : ",end="") 
print (s) 
print ("The reversed string is : ",end="") 
print (reverse(s)) 