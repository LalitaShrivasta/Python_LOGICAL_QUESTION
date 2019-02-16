user=int(raw_input("enter a number"))
rev=0
while user>0:
    dig=user%10
    rev=rev*10+dig
    user=user//10
print ("Reverse of the number:",rev)    
