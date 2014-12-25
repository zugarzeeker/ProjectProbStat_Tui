import random
from normalCards import deck

HOO_BIG_RED = ['1_king_red','2_airplane_red','3_eleplant_red']
HOO_BIG_BLACK = ['1_king_black','2_airplane_black','3_eleplant_black']

def printCardsPlayers(players):
    print '=' * 150
    for playerCards in players :
        playerCards.sort()
        cardString = ''
        for card in playerCards :
            cardString += card + ' '
        print 'player' + str(players.index(playerCards)+1) + ' ---> ' + cardString

def removeCards(cards, removeList):
    for item in removeList :
        while cards.count(item) != 0:
            cards.remove(item)
    return cards

def randomCards(cards, removeList):
    cards = removeCards(cards, removeList)
    random.shuffle(cards)
    while set(['1_king_red','2_airplane_red','3_eleplant_red']).issubset(cards[0:4]) :
        random.shuffle(cards)

    temp = [x for x in removeList[1:]]
    random.shuffle(temp)
    temp = removeList + temp
    inHand = temp[:4]+ cards[:4]
    outHand = cards[4:] + temp[4:]
    random.shuffle(outHand)

    cards = inHand + outHand
    return cards

def createPlayersHand(players, cards):
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    return players

def cardsCheckUpper(players):
    for player in players:
        if players.index(player) != 0 :

            if player.count('1_king_red') == 1 :
                if player.count('2_airplane_red') >= 2 and player.count('3_eleplant_red') >= 1 \
                or player.count('2_airplane_red') >= 1 and player.count('3_eleplant_red') >= 2 :
                    return 1

    return 0

samapleSpace = 100000.0
event = 0.0
for round in range(1, int(samapleSpace+1)):
    hoo_little_red= ['1_king_black', '2_airplane_black', '3_eleplant_black']
    players = []
    cards = deck()
    cards = randomCards(cards, hoo_little_red)
    players = createPlayersHand(players, cards)
    event += cardsCheckUpper(players)
    printCardsPlayers(players)
    players = []

print '=' * 150
print 'event ' + str(event)
print 'samapleSpace ' + str(samapleSpace)
print str(event / samapleSpace * 100) + ' %'