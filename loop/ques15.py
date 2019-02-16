sum=0
a=0
while a<=4:
    num=int(raw_input("enter a number"))
    sum=sum+num
    a=a+1
print sum

# ...............................................

num1=int(raw_input("enter a number"))
sum=0
while True:
    a=num1%10
    num1=num1/10
    sum=sum+a
    if num1<10:
        sum=sum+num1
        break
print sum    