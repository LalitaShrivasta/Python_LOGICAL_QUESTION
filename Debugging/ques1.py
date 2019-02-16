# question 1...........
print "We will learn debugging by removing all the errors from this python"

# question_2..........
year = 2016
name = "NavGurukul"
print name + ', ' + "mein start hua tha!"

# question_3.........
price_milk = raw_input("1L milk ka price daalo?")
print "10L milk " + price_milk*10 + " rupees ka aata hai."

# question_4............
number = float(raw_input("please enter a decimal number"))
print "your number divided by 2 is equal to = ",number/2

# question_5.............
#Tumhare paas 5 mangoes hai
mangoes = 5
# Kisi ne humhe 5 aur mangoes de diye
manGoes = mangoes + 5
# Ab tumne unn mangoes ko 5 logo mei baant diya
print manGoes / 5
# Par isse toh 1 mango hi mila. Par milne 2 chahiye the. Code ko sahi karo jisse ki sabko sahi mangoes mile.

# question_6.............
# Aapke paas ek variable mein `raw_input` se gaadi ki speed ka ek integer hai
speed = int( raw_input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
if speed <=60:
    print "Speed kam hai"
elif speed >=30:
    print "Speed bahot kam hai"
elif speed > 100:
    print "Speed bahot fast hai"

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho
# ki kya problemn hai.


