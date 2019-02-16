def check_number_list(num1,num2):
    i=0
    while i<len(num1):
        b=num1[i]
        c=num2[i]
        if b%2==0 and c % 2 == 0:
            print"dono even hai"
        else:
            print "dono even nhi hai"    
        i=i+1
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87] )            
