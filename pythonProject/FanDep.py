# fanName=['usha','bajaj','crompten']
# fanNo=[100,100,100]

# def names (no):
#     for x in range(1,no+1):
#         fanName.append(raw_input('enter the '+str(x) +' name : '))
#         fanNo.append(raw_input('enter the count : '))

# iP= int(raw_input('Enter How many type you have ? : '))
# names(iP)
# data = zip(fanName,fanNo)

data = {'usha' : 100,'bajaj': 100,'crompton' : 100} #dictionary

dependName = ['usha','bajaj','crompton'] #dependancy usha 2-> bajaj 4 -> crompton 5
dependCount = [2,3,4]
printList= []
day1 = 100 #need to install 100 fans in a day

def ror (name,no):
    for x in range(1,no+1):
        printList.append(name) #add names to the print list
        data[name]=data[name]-1    #this will minus 1 from each time adding to print list 
        if len(printList)==day1: 
            break


for x in range (0,day1):
    for y in range(0,(len(dependName))):
        ror(dependName[y],dependCount[y])
        if len(printList)==day1:
            break
    if len(printList)==day1:
            break


data['usha']=data['usha']-10
print ('you need to install your todays '+ str(day1) + ' fans in this order ')
print  (printList)
print ('remeaning fans in hand as follows')
print (data)

