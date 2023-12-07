print('Accesing cards file')
with open('04/input.txt') as file:
    lines=file.readlines()

def getWinnigNumbers(card): #Gets the wining numbers of a card
    winnigNumbers=card[10:39]
    list=str(winnigNumbers).split(' ')
    result=[x for x in list if x != ''] #clean up of ''
    return result

def getNubersInCard(card): #Gets the number corresponding to the card
    numberInCard=card[42:116]
    list=str(numberInCard).split(' ')
    result=[x for x in list if x != '']#clean up of ''
    return result

def calculateCardPoints(card): #calculate the points of the card
    cardPoints=0
    winnersInCard=[]
    winningNumbers=getWinnigNumbers(card)
    cardNumbers=getNubersInCard(card)
    for index in cardNumbers:
        if cardPoints==0 and index in winningNumbers:
            cardPoints=1
        elif index in winningNumbers:
            cardPoints*=2
            
    return cardPoints

def solvePart1():
    points=0
    for card in lines:
        points+=int(calculateCardPoints(card))
        #print('points: '+ str(points))
    return points

print('Part 1: ' + str(solvePart1()))

def getCardNumber(card): #Returns the number a card
    result=card[5:8]
    result.strip()
    return int(result)

def countCardsToDraw(card): #Returns how many card to draw from one scratchcard
    winningNumbers=getWinnigNumbers(card)
    cardNumbers=getNubersInCard(card)
    counter=0
    for number in cardNumbers:
        if(number in winningNumbers):
            counter+=1
    return counter

def drawCloneCards(cardsInHand,i,j): #draws j copies of cards starting from position i and returns a new 'cardsInHand' with them on it
    for x in range(j):
        cardsInHand.append(lines[i+x])
    return cardsInHand

def solvePart2():
    hand=[1 for i in range(len(lines))]
    for card in lines:
        cardNumber=getCardNumber(card)
        cardsToDraw=countCardsToDraw(card)
        for i in range(cardNumber, cardNumber+cardsToDraw):
            if i < len(hand):
                hand[i]+=1*hand[cardNumber-1]
    return sum(hand)

print('Part 2: '+str(solvePart2()))

