#in this logic fan dependency order should be  ordered in dic   


data = ['f1','f2','f3','f4'] #dictionary

dependency = {'f1':['f2','f3','f4'],'f2':['f3','f4'],'f3':['f4']} #dependacy
printList= [] #fan order saves here

def findDepen ():
    for x in range (0,len(data)): 
        if data[x] not in printList: #for skiping printlist alredy in items
            a=dependency[data[x]] #get list from dependency pointer to a variable
            if a[0] == printList[len(printList)-1]: # checking printList last elemnt == 1st element of dependency 
                printList.append(data[x]) 

for x in range (0,len(data)):
    if data[x] not in dependency: #to find not avilable charecter in dependancy that is the 1st 
        printList.append(data[x])


while True:
    findDepen()
    if(len(data) == len(printList)): #fan number and fan order number equals loop break 
        break

print (printList)


