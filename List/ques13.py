a=10
b=[]
while a>0:
    num=int(raw_input("enter a nuber"))
    b.append(num)
    a=a-1
i=0
rev=-1
c=[]
while i<len(b):
     c.append(b[rev])
     rev=rev-1
     i+=1
print(c) 

