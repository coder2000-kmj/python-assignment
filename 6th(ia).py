m1,m2,m3=input("Enter your first,second and third Ia marks")
int(m1)
int(m2)
int(m3)

if m1>m2:
    if m2>m3:
        print("The average is ",(m1+m2)/2)
    else:
        print("The average is ",(m1+m3)/2)
else:
    if m2>m3:
        print("The average is ",(m1+m2)/2)
    else:
        print("The average is ",(m2+m3)/2)
