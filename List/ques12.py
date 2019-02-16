a=5
b=[]
while a>0:
    num=int(raw_input("enter a number"))
    a=a-1
    b.append(num)
    num1=int(raw_input("enter a number"))
    if num1 in b:
        print "yes! it is in this list"
    else:
        print "No! it is not present in this link" 
        print (b) 
  