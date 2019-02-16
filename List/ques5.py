a=10
b=[]
while a>0:
    num1=int(raw_input("enter a number"))
    b.append(num1)
    a=a-1
    num2=int(raw_input("enter a number"))
    if num2 in b:
        print b
        print "yes this number present in list"
        # print b
    else:
        print "No it is not present in list"    
        
