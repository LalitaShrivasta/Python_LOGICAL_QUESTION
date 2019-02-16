question_list = [
	"How many continents are there?",  			
	"What is the capital of India?",
	"NG mei kaun se course padhaya jaata hai?"	
]

options_list = [
	#pehle question ke liye options
	["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    # ["3.seven","4.Eight"],
	#second question ke liye options
	["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    # ["2.Bhopal", "4.Delhi"],
	#third question ke liye options
	["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"],
    # ["1.Software Engineering", "2.Counseling"]
]
lifeline_list=["2.Nine","3.Seven","2.Bhopal","4.Delhi","1.Software Engineering","Tourism"]
helpline = 5050
solution_list=[3,4,1]
i=0
while i<len(question_list):
    print question_list[i] 
    j=0
    while j<len(options_list[i]):
        print options_list[i][j]
        j=j+1
    num=int(raw_input("enter your answer which you think that is right"))
    if num==solution_list[i]:
        print "congrats aapka answer sahi hai"
    # elif  num!= solution_list:
    #     print "out"
    #     break
       
   
    if num == helpline:
        print lifeline_list[],lifeline_list[i] 
        num1 = int(raw_input("enter your correct answer"))
        # print solution_list[0]
        print "your ans is correct..congrats"  
    else:    
         if num1 != solution_list[0]:
            print "sorry your ans is wrong now you are out of the game"
            break       
    i=i+1