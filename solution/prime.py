a=int(input("enter any number"))
b=0
for i in a:
    if(b%i==0):
        print("this is not prime number")
        break
    if(i==b):
        print("this is prime number")
        
