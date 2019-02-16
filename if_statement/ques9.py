water=int(raw_input("enter a letter"))
if water<1:
    print "paani bharna hai"
elif water<10:
    print "nahi bharna hai"
else:
    if water>10:
        print "overflow"
