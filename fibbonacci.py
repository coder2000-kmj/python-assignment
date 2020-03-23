# python program to generate first n Fibonacci number and factorial of n using functions 
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("should be greater than zero") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
#main code
n = int(input('Enter a number: '))
f=fact(n)

print("{}!={}".format(n,f))
print( "Fibonacci number" )
print(fibonacci(n))
