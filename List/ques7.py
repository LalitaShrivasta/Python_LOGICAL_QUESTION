a=10
b=[]
while a>0:
    num1=int(raw_input("enter a number"))
    b.append(num1)
    a=a-1
i = 0
rev = -1
v = []
while i < len(b):
    v.append(b[rev])
    rev = rev-1
    i += 1
print v
