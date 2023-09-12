a=float(input("enter the value"))
b=float(input("enter the value"))
c=float(input("enter the value"))
d=(b**2)-(4*a*c)
print("the value of discriminent",d)
if d>0:
    print{-b+sqrt(b**2-4*a*c)/2*a}
elif d==0:
    print(-b/2*a)
else:
    print{-b-sqrt(b**2-4*a*c)/2*a}

