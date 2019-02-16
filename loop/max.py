def condition():
    if(list[i]==list[3] or list[i]==list[4]):
        print(max)
list=[2,8,7,9,10,34]
max=list[2]
i=0
while(i<len(list)):
    if(max>list[i]):
        condition()
        max=max
    else:
        condition()
        max=list[i]
    i=i+1
