''' This is a simple blackjack app written in python '''
import random, os, sys

cardName = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}
cardSuit = {'c': '♧', 'h': '♡', 's': '♤', 'd': '♢'}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return cardName[self.rank] + " " + cardSuit[self.suit]

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if self.rank > 9:
            return 10
        else:
            return self.rank


def showHand(hand):
    for card in hand:
        print(card)


def showCount(hand):
    print("TOTAL: " + str(handCount(hand)))


def handCount(hand):
    handCount = 0
    for card in hand:
        handCount += card.BJValue()
    return handCount


def gameEnd(score):
    print("*FINAL SCORE* Computer: " + str(score['computer']) + " You: " + str(score['human']))
    sys.exit(0)


deck = []
suits = ['c', 'h', 'd', 's']
score = {"computer": 0, "you": 0}
hand = {"computer": [], "you": []}

for suit in suits:
    for rank in range(1, 14):
        deck.append(Card(rank, suit))

keepPlaying = True

while keepPlaying:

    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    # Deal Cards

    hand["you"].append(deck.pop(0))
    hand["computer"].append(deck.pop(0))

    hand["you"].append(deck.pop(0))
    hand["computer"].append(deck.pop(0))

    playHuman = True
    bustedHuman = False

    while playHuman:
        os.system('clear')
        print("Computer: " + str(score["computer"]) + " You: " + str(score["you"]))

        print()

        print('Computer Shows: ' + str(hand["computer"][-1]))
        print()

        print("Your Hand:")

        showHand(hand["you"])

        showCount(hand["you"])

        print()

        inputCycle = True
        userInput = ""

        while inputCycle:
            userInput = input("(H)it, (S)tand, or (Q)uit: ").upper()
            if userInput == "H" or "S" or "Q":
                inputCycle = False

        if userInput == "H":
            hand["you"].append(deck.pop(0))
            if handCount(hand["you"]) > 21:
                playHuman = False
                bustedHuman = True
        elif userInput == "S":
            playHuman = False
        else:
            gameEnd(score)

    playComputer = True
    bustedComputer = False

    while not bustedHuman and playComputer:
        print(handCount(hand["computer"]))
        if handCount(hand["computer"]) < 17:
            hand["computer"].append(deck.pop(0))
        else:
            playComputer = False

        if handCount(hand["computer"]) > 21:
            playComputer = False
            bustedComputer = True

    if bustedHuman:
        print("You're busted")
        score["computer"] += 1
    elif bustedComputer:
        print("Computer is busted")
        score["you"] += 1
    elif handCount(hand['human']) > handCount(hand["computer"]):
        print("You win")
        score["you"] += 1
    else:
        print("Computer Wins")
        score["computer"] += 1

    print()
    print("Computer Hand:")
    showHand(hand["computer"])
    showCount(hand["computer"])

    print()
    print("Your Hand:")
    showHand(hand["you"])
    showCount(hand["you"])
    print()
    if input("(Q)uit or enter for next round").upper() == 'Q':
        gameEnd(score)

    deck.extend(hand["computer"])
    deck.extend(hand["you"])

    del hand["computer"][:]
    del hand["you"][:]
