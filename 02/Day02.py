baseBag =[12,13,14] #Red, Green, Blue

print('Accesing calibration file')
with open('02/input.txt') as file:
    lines=file.readlines()

import re

def CleanString(string): #remove game number and split the string in the different draws
    cleaned=string[8:]
    cleaned=cleaned.split(';')
    for i in range(len(cleaned)):
        cleaned[i]=cleaned[i].split(',')
        for j in range(len(cleaned[i])):
            cleaned[i][j]=cleaned[i][j].replace(' ', '')
    return cleaned



def removeColor(string): #remove color indicator leaving only the number
    return re.sub("[^0-9]", "", string)

#test=CleanString(testString)


def Check(bag, stringToCheck): #check a string and returns a list with the corresponding numbers representing a draw
    match re.sub('[^a-zA-Z]+', '', stringToCheck):
        case 'red':
            bag[0]=bag[0]+int(removeColor(stringToCheck))
        case 'green':
            bag[1]=bag[1]+int(removeColor(stringToCheck))
        case 'blue':
            bag[2]=bag[2]+int(removeColor(stringToCheck))
    return bag

def BagIsPosible(bag): #check if the bag is posible with the base number of cubes
    result=True
    for i in range(3):
        result=result and bag[i]<=baseBag[i]
    return result

def compareBags(bag1, bag2): #compares two bags and returns one with the higest number of each acolor
    for i in range(3):
        if(bag1[i]<bag2[i]):
            bag1[i]=bag2[i]
    return bag1

def readLine(line): #reads a line and returns de representaion of the data in it
    cBag=[0,0,0]
    for draw in line:
        bagOfDraw=[0,0,0]
        for element in draw:
            bagOfDraw=Check(bagOfDraw,element)
        cBag=compareBags(cBag,bagOfDraw)    
    return cBag

def part1(): #Solves part 1
    counter=0
    for index in range(len(lines)):
        x=readLine(CleanString(lines[index]))
        if(BagIsPosible(x)):
            counter+=index+1
    return counter

def setPower(setX): #calculates de power of a ceritan set (multiply all the values)
    power=1
    for value in setX:
        power*=value
    return power

def part2(): #Solves part 2
    counter=0
    for index in range(len(lines)):
        x=readLine(CleanString(lines[index]))
        counter+=setPower(x)
    return counter

print('Part 1: '+ str(part1()))

print('Part 2: '+ str(part2()))