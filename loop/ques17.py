guss=5
a=0
while a<5:
    user=int(raw_input("enter a number between (1 to 10)"))
    if user==5:
        print "your guess is right"
        break
    elif user ==0:
        print "you are not enter a valid number"
    elif user==3:
        print " your guess is wrong try again"
    else:
        print "user ne guess sahi nhai kiya hai" 
                  