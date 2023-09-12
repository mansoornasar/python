print("1.Add")
print("2.Sub")
print("3.multi")
print("4.sub")
c=int(input("enter your choice"))
a=int(input("enter a number"))
b=int(input("enter a number"))
if c==1:
    result=a+b
    print(result)
elif c==2:
    result=a-b
    print(result)
elif c==3:
    result=a*b
    print(result)
elif c==4:
    result=a/b
    print(result)
else:
    print(invalid)
