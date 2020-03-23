'''
Write a program to prompt the user for hours and rate per hour to
compute gross pay. Also to give the employee 1.5 times the hourly rate for
hours worked above 40 hours
To find the average of best two IA  of 3 IA.
'''
h=float(input("Enter the number of hours"))
rate=150 #hourly rate
if h<=40:
    print("The gross pay is: ",h*rate)
elif h>=40:
    print("Your gross pay is: ",(40*rate)+(h-40)*1.5*rate)
