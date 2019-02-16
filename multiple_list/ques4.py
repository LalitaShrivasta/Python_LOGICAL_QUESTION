a=5
b=[]
while a>0:
    num=int(raw_input("enter a number"))
    if num%2==0:
        b.append(num)
    a=a-1    
print b
