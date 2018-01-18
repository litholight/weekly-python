import re

def give_me_file(thisFile):
    #listOfDicts =[]
    fileName = str(thisFile + ".txt")
    print(fileName)
    file1 = open(fileName, 'r')

    logString = file1.read()
    file1.close()
    
    regex = r'[0-9]{2,3}\.[0-9]+\.[0-9]+\.[0-9]'

    matches = re.finditer(regex, str(logString))

    return matches

fileName = input("What is the logfile name?")

listOfDicts = []
myDict = None 
for match in give_me_file(fileName):
    if match.group() == '10.0.356.0':
        next
    else:
        myDict = {'ip_address': match.group(), 'line number': len(listOfDicts)+ 1}
        listOfDicts.append(myDict)
print(str(listOfDicts) + str(len(listOfDicts)))
