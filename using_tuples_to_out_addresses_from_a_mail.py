from audioop import reverse
from pickle import TRUE


mailList = []
mailDict = {}

with open (input ("please input the name of the folder :\n")) as fName:
    for check in fName:
        mailList = check.split()
        if check.startswith('From'):
            mail = mailList [1]
            if mail not in mailDict:
                mailDict[mail] = 1  #adding a new value
            else:
                mailDict[mail] += 1  #if present just add to the count
    #print (mailDict)


Dlist = list()
for mail,count in (mailDict.items()):
    Dlist.append((count,mail))  #attaching the key and value of the dict to a list
    
Dlist.sort(reverse=True)  #re-arrange from the highest to the lowest
print (Dlist)

lmax = max(Dlist)  #to pick highest value

print ('the person with the most count is ',lmax)
