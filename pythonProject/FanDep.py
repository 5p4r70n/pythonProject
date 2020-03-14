#in this logic fan dependency order should be  ordered in dic   


data = ['f1','f2','f3','f4'] #dictionary

dependency = {'f1':['f2','f3','f4'],'f2':['f3','f4'],'f3':['f4']} #dependacy
printList= [] #fan order saves here

def findDepen ():
    for x in range (0,len(data)): 
        if data[x] not in printList: #for skiping printlist alredy in items
            if (set(printList)==set(dependency[data[x]])) == True: # this will cehck the two lists are equal or not
                printList.append(data[x])

for x in range (0,len(data)):
    if data[x] not in dependency: #to find not avilable charecter in dependancy that is the 1st 
        printList.append(data[x])


while True:
    findDepen()
    if(len(data) == len(printList)): #fan number and fan order number equals loop break 
        break

print (printList)