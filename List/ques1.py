numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
list_lenght=len(numbers)
a=0
more_than20=0
less_than40=0
while a <list_lenght:
    marks=numbers[a]
    if marks < 40 and marks >20:
        more_than20=more_than20 +1
    a=a+1
print "more_than 20" + str(more_than20)
print "less_than 40" + str (less_than40)           
