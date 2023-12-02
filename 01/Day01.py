print('Accesing calibration file')
with open('01/input.txt') as file:
    lines=file.readlines()

sumvalue1=0
sumvalue2=0

def decodeLine(lineToDecode):
    #Flags for when the numbers are found
    first=False
    last=False 

    size=len(lineToDecode) #size of the line
    
    #default numbers
    firstNumber=0
    lastNumber=0
    for i in range(size):
        if(not first and lineToDecode[i].isdigit()):
            #print('Found first: '+ str(lineToDecode[i]))
            first=True
            firstNumber=lineToDecode[i]
        if(not last and lineToDecode[size-1-i].isdigit()):
            #print('Found last :'+ str(lineToDecode[size-1-i]))
            last=True
            lastNumber=lineToDecode[size-1-i]
        if(first and last):
            break
    code=int(firstNumber)*10+int(lastNumber)
    #print('Code:' + str(code))
    return(code)

for index in lines:
     sumvalue1+=int(decodeLine(index))

print('Part 1: '+ str(sumvalue1))

#Modifiying line for part 2
def replasingStrings(line):
    line=line.replace('one', 'o1e')
    line=line.replace('two', 't2o')
    line=line.replace('three', 'th3ee')
    line=line.replace('four', 'f4r')
    line=line.replace('five', 'f5e')
    line=line.replace('six', 's6x')
    line=line.replace('seven', 's7n')
    line=line.replace('eight', 'e8t')
    line=line.replace('nine', 'n9e')
    return(line)

for index in lines:
    sumvalue2+=int(decodeLine(replasingStrings(index)))
print('Part 2: '+ str(sumvalue2))