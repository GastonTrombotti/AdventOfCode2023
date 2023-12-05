print('Accesing cards file')
with open('04/input.txt') as file:
    lines=file.readlines()

testString='Card   1: 10  5 11 65 27 43 44 29 24  6 | 65 10 18 14 17 97 95 34 38 23 10 25 22 15 87  9 28 43  4 71 89 20 72  5  6\n'

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
    #winnersInCard=[x for x in winningNumbers if x in cardNumbers]

    #if(winnersInCard!=[]): #check if it's empty
    #    cardPoints=1
    #    for hit in winnersInCard[1:]:
    #        cardPoints*=2
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
        print('points: '+ str(points))
    return points
print(getWinnigNumbers(testString))
print(getNubersInCard(testString))
winningNumbers=getWinnigNumbers(testString)
cardNumbers=getNubersInCard(testString)
winnersInCard=[x for x in winningNumbers if x in cardNumbers]
print(winnersInCard)
print(calculateCardPoints(testString))
print(solvePart1())

