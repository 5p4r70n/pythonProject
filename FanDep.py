while True:
    try:
        FanNo= int(raw_input("Hai! Sooraj Welcome to fan Positin Finder,Enter your Fan Count : "))
        Depend= int(raw_input("Which direction you are going to install fans If Acending then 0 ,decending then 1 : "))
        assert (FanNo >0 and (Depend== 0 or 1))
        break
    except:
        print("this is a string or not acceptable range Try again")
if Depend==0 : 
    print ("Install Fan in this Order")   
    for x in range(1,(FanNo+1)) :
        print ("fan"+str(x))
if Depend==1 :
    print("Install Fan in This Order")
    for x in  reversed(range (1,(FanNo+1))) :
        print ("fan"+str(x))

def acending(no) : 
    print("make sure to install these fans on the given order before fan"+str(no))    
    for x in range (1,no):
        print ("Fan"+str(x))
    print("Order for the next fan instalations after fan"+str(no))
    for x in range (no+1,FanNo+1):
        print ("Fan"+str(x))

def decending(no) :
    print("make sure to install these fans on the given order before fan"+str(no))    
    for x in reversed(range (no+1,FanNo+1)) :
        print ("Fan"+str(x))
    print("Order for the next fan instalations after fan"+str(no))
    for x in reversed( range (1,no)):
        print ("Fan"+str(x))

while True:
    try:
        FanIns = int(raw_input("which fan you want to install first, Enter fan no : "))
        assert(FanIns > 0 and FanIns <= FanNo)
        break
    except:
        print("something phishy try again")
if Depend==0 :
    if FanIns == 1 :
        print("it is the first fan no dependency check needed")
    else:
        acending(FanIns)
if Depend==1 :
    if FanIns == FanNo :
        print("it is the first fan no dependency check needed")
    else:
        decending(FanIns)