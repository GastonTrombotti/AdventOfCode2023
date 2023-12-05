print('Accesing engine schematic file')
with open('03/input.txt') as file:
    lines=file.readlines()

maxLen=len(lines[0])-1
maxHeight=len(lines)-1

def searchParts(): #Searches for parts in the schematic
    results=[]
    for i in range(len(lines)):
        #print('line: '+ str(lines[i]))
        for j in  range(maxLen):
            #print('character: '+ str(lines[i][j]))
            if not(lines[i][j].isdigit()) and lines[i][j]!='.':
                #print('found part: '+ str(lines[i][j]))
                results.append((i,j))
                
#    print(results)
    return results

directions=searchParts()

def getCode(i,j,z): #obtains a code in the positions (i, j) to (i,z)
    result=lines[i][j]
    if(z>j):
        for p in range(z-j):
            result+=lines[i][j+p+1]
    return(int(result))

def searchCodes(): #Returns a list of codes of the different parts
    codes=[]
    for i in range(len(directions)):
        pointX=int(directions[i][0])
        pointY=int(directions[i][1])
        startingPosition=pointY
        endingPosition=pointY
        if(pointX>0):
            startingPosition=pointY-1
            endingPosition=pointY-1
            if(lines[pointX-1][pointY-1].isdigit()):
                while(lines[pointX-1][startingPosition-1].isdigit()):
                    startingPosition-=1
                while(lines[pointX-1][endingPosition+1].isdigit()):
                    endingPosition+=1
                codes.append(getCode(pointX-1,startingPosition,endingPosition))
            if(endingPosition<pointY and lines[pointX-1][pointY].isdigit()):
                startingPosition=pointY
                endingPosition=pointY
                while(lines[pointX-1][endingPosition+1].isdigit()):
                    endingPosition+=1
                #print('X: '+ str(pointX-1)+ 'y: '+ str(startingPosition) +' to '+str(endingPosition))
                codes.append(getCode(pointX-1,startingPosition,endingPosition))
            if(endingPosition<pointY+1 and pointY+1<maxLen):
                if(lines[pointX-1][pointY+1].isdigit()):
                    startingPosition=pointY+1
                    endingPosition=pointY+1
                    while(endingPosition+1<maxLen and lines[pointX-1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    codes.append(getCode(pointX-1,startingPosition,endingPosition))
        if(pointY>0):
            startingPosition=pointY-1
            endingPosition=pointY-1
            if(lines[pointX][pointY-1].isdigit()):
                while(startingPosition>0 and lines[pointX][startingPosition-1].isdigit()):
                    startingPosition-=1
                codes.append(getCode(pointX,startingPosition,endingPosition))
        if(pointY<maxLen):
            startingPosition=pointY+1
            endingPosition=pointY+1
            if(lines[pointX][pointY+1].isdigit()):
                while(endingPosition<maxLen and lines[pointX][endingPosition+1].isdigit()):
                    endingPosition+=1
                codes.append(getCode(pointX,startingPosition,endingPosition))
        if(pointX<len(lines)-1):
            startingPosition=pointY-1
            endingPosition=pointY-1
            if(lines[pointX+1][pointY-1].isdigit()):
                while(lines[pointX+1][startingPosition-1].isdigit()):
                    startingPosition-=1
                while(lines[pointX+1][endingPosition+1].isdigit()):
                    endingPosition+=1
                codes.append(getCode(pointX+1, startingPosition,endingPosition))
            if(endingPosition<pointY and lines[pointX+1][pointY].isdigit()):
                startingPosition=pointY
                endingPosition=pointY
                while(lines[pointX+1][endingPosition+1].isdigit()):
                    endingPosition+=1
                codes.append(getCode(pointX+1, startingPosition,endingPosition))
            if(endingPosition<pointY+1 and lines[pointX+1][pointY+1].isdigit()):
                startingPosition=pointY+1
                endingPosition=pointY+1
                while(endingPosition<maxLen and lines[pointX+1][endingPosition+1].isdigit()):
                    endingPosition+=1
                codes.append(getCode(pointX+1, startingPosition,endingPosition))
    return codes

def searchGearCodes(): #Solves part2, finds the gears and calculates de sum of codes
    codesList=[]
    for i in range(len(directions)):
        pointX=int(directions[i][0])
        pointY=int(directions[i][1])
        startingPosition=pointY
        endingPosition=pointY
        counter=0
        codes=[]
        gearSum=0
        if(lines[pointX][pointY]=='*'):
            if(pointX>0):
                startingPosition=pointY-1
                endingPosition=pointY-1
                if(lines[pointX-1][pointY-1].isdigit()):
                    while(lines[pointX-1][startingPosition-1].isdigit()):
                        startingPosition-=1
                    while(lines[pointX-1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    codes.append(getCode(pointX-1,startingPosition,endingPosition))
                    counter+=1
                if(endingPosition<pointY and lines[pointX-1][pointY].isdigit()):
                    startingPosition=pointY
                    endingPosition=pointY
                    while(lines[pointX-1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    #print('X: '+ str(pointX-1)+ 'y: '+ str(startingPosition) +' to '+str(endingPosition))
                    codes.append(getCode(pointX-1,startingPosition,endingPosition))
                    counter+=1
                if(endingPosition<pointY+1 and pointY+1<maxLen):
                    if(lines[pointX-1][pointY+1].isdigit()):
                        startingPosition=pointY+1
                        endingPosition=pointY+1
                        while(endingPosition+1<maxLen and lines[pointX-1][endingPosition+1].isdigit()):
                            endingPosition+=1
                        codes.append(getCode(pointX-1,startingPosition,endingPosition))
                        counter+=1
            if(pointY>0):
                startingPosition=pointY-1
                endingPosition=pointY-1
                if(lines[pointX][pointY-1].isdigit()):
                    while(startingPosition>0 and lines[pointX][startingPosition-1].isdigit()):
                        startingPosition-=1
                    codes.append(getCode(pointX,startingPosition,endingPosition))
                    counter+=1
            if(pointY<maxLen):
                startingPosition=pointY+1
                endingPosition=pointY+1
                if(lines[pointX][pointY+1].isdigit()):
                    while(endingPosition<maxLen and lines[pointX][endingPosition+1].isdigit()):
                        endingPosition+=1
                    codes.append(getCode(pointX,startingPosition,endingPosition))
                    counter+=1
            if(pointX<len(lines)-1):
                startingPosition=pointY-1
                endingPosition=pointY-1
                if(lines[pointX+1][pointY-1].isdigit()):
                    while(lines[pointX+1][startingPosition-1].isdigit()):
                        startingPosition-=1
                    while(lines[pointX+1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    codes.append(getCode(pointX+1, startingPosition,endingPosition))
                    counter+=1
                if(endingPosition<pointY and lines[pointX+1][pointY].isdigit()):
                    startingPosition=pointY
                    endingPosition=pointY
                    while(lines[pointX+1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    #print(getCode(pointX+1, startingPosition,endingPosition))
                    codes.append(getCode(pointX+1, startingPosition,endingPosition))
                    counter+=1
                if(endingPosition<pointY+1 and lines[pointX+1][pointY+1].isdigit()):
                    startingPosition=pointY+1
                    endingPosition=pointY+1
                    while(endingPosition<maxLen and lines[pointX+1][endingPosition+1].isdigit()):
                        endingPosition+=1
                    codes.append(getCode(pointX+1, startingPosition,endingPosition))
                    counter+=1
            if(counter==2):
                codesList.append(codes)
    for gear in codesList:
        gearMultiplier = gear[0]*gear[1]
        gearSum+=gearMultiplier

    return gearSum

def part1(): #solves part1
    codes=searchCodes()
    results=0
    for i in codes:
        results+=i
    return results
print('Part 1: ' +str(part1()))

print('Part 2: '+str(searchGearCodes()))
