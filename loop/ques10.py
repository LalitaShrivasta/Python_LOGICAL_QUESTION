# sum=0
# a=11
# while a>0:
#     num=int(raw_input("enter your weight"))
#     sum=sum+num
#     a=a-1
# else:
#     if sum%5==0:  
#        print "Average weight is :",sum/11.0  
#         # print "ya the average weight is divisible by 5"  
count =0
sum =0 
while count <11:
    inp = input("enter a weight")
    sum = sum+inp
    count = count+1
avg= sum/11.0
if avg % 5==0:
    print "avg is divisible by 5"
else:
    print "the avg is", avg    
    print "no it is not divisible by 5"
