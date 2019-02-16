a=[[1,2,3,4,5,6],[8,65,34,23,56,58]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        b=a[i][j]
        sum=sum+b
        j=j+1
    i=i+1    
    print b
    print sum