list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
while i<len(list1):
    if list1[i] in list2:
        print list1[i]
    i=i+1    