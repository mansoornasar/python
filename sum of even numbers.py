a=int(input("enter a number"))
sum=0
while a!=0:
     d=a%10
     if d%2==0:
        sum=sum+d
     a=a//10
print("sum is",sum)

