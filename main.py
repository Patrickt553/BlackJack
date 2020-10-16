import random
import sys

suit = ["Clubs", "Hearts", "Spades", "Diamonds"]
usedCards = []
playing = True


class Player():
    def __init__(self, hand, handvalue):
        self.hand = hand
        self.handvalue = handvalue


playerHand = []
playerHandValue = []

dealerHand = []
dealerHandValue = []

dealer = Player(dealerHand, dealerHandValue)
player1 = Player(playerHand, playerHandValue)

while playing:

    if sum(player1.handvalue) > 21:
        print("Bust! Play again?")
    else:
        if input("Y/N -- ") == str.lower('Y'):
            playerHandValue = []
            usedCards = []
        else:
            sys.exit()


    def dealerCard():

        global dealercard
        global dealervalue

        dealercardSuit = suit.__getitem__(random.randint(0, 3))
        dealernumber = random.randint(1, 13)
        dealercardNumber = dealernumber
        dealervalue = dealernumber

        if (dealercardNumber > 1) and (dealercardNumber <= 10):
            dealercardNumber = str(dealernumber)

        elif dealercardNumber == 1:
            dealercardNumber = str("Ace")
            if sum(playerHandValue) <= 10:
                dealervalue = 11
            else:
                dealervalue = 1
        elif dealercardNumber == 11:
            dealercardNumber = str("Jack")
            dealervalue = 10

        elif dealercardNumber == 12:
            dealercardNumber = str("Queen")
            dealervalue = 10

        elif dealercardNumber == 13:
            dealercardNumber = str("King")
            dealervalue = 10

        dealercard = dealercardNumber + dealercardSuit

        if dealercard in usedCards:
            dealerCard()

        else:
            usedCards.append(dealercard)
            if len(dealerHand) > 1:
                print("Dealer: " + dealercardNumber + ' of ' + dealercardSuit + '---- ' + str(dealervalue))
            else:
                pass

    def getCard():

        global value
        global card

        cardSuit = suit.__getitem__(random.randint(0, 3))
        number = random.randint(1, 13)
        cardNumber = number
        value = number


        if (cardNumber > 1) and (cardNumber <= 10):

            cardNumber = str(number)
        elif cardNumber == 1:
            cardNumber = str("Ace")
            if sum(playerHandValue) <= 10:
                value = 11
            else:
                value = 1
        elif cardNumber == 11:
            cardNumber = str("Jack")
            value = 10

        elif cardNumber == 12:
            cardNumber = str("Queen")
            value = 10

        elif cardNumber == 13:
            cardNumber = str("King")
            value = 10
        card = cardNumber + cardSuit

        if len(usedCards) == 52:
            print("There are no more cards in the deck.")
            print("There are " + str(len(usedCards)) + " in the discard pile.")

        elif card in usedCards:
            usedCards.append(card)

        else:
            usedCards.append(card)
            print("You: " + cardNumber + ' of ' + cardSuit + '---- ' + str(value))


    playerChoice = input("---------------------------------------\n"
                         "What would you like to do?\n"
                         "1. Hit\n"
                         "2. Hand\n"
                         "3. Stay\n"
                         "4. Quit\n"
                         ">>> ")

    print("Your hand: " + str(player1.hand))
    print(sum(player1.handvalue))
    # if len(dealerHand) > 1:
    # print("Dealer's hand: " + str(sum(dealer.handvalue) - sum(dealer.handvalue)[0]))

    if playerChoice == ("discard"):
        print(str(len(usedCards)))

    elif playerChoice == ('Hit'):
        getCard()
        playerHand.append(card)
        playerHandValue.append(value)

    if sum(dealerHandValue) < 17:
        dealerCard()
        dealerHand.append(dealercard)
        dealerHandValue.append(dealervalue)

    elif playerChoice == ('Stay'):
        if sum(dealerHandValue) >= 17:
            dealerCard()
            if sum(dealerHandValue) > 21:
                print("\n"
                      "Dealer busts! You win!\n")
                print(sum(dealerHandValue))

            elif sum(dealerHandValue) > sum(playerHandValue):
                print("Dealer Wins! Better luck next time!")
                print(sum(dealerHandValue))

            else:
                print(sum(dealerHandValue))
                print("\n"
                      "You win!")

    elif playerChoice == ("hand"):
        print(player1.hand)

    elif playerChoice == ("quit"):
        sys.exit()
else:
    sys.exit()
