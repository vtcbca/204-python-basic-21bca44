a=int(input("enter any number"))
sum=0
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of it is :",sum)
