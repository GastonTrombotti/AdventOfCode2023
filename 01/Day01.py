print('Accesing calibration file')
with open('01/input.txt') as file:
    lines=file.readlines()

linesValue=[]
sumvalue=0

def decodeLine(lineToDecode):
    first=False
    last=False
    size=len(lineToDecode)
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
    print('Code:' + str(code))
    return(code)

for index in lines:
     sumvalue+=int(decodeLine(index))

print('Sum of all values: '+ str(sumvalue))