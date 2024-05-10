import random
import copy
from game_center import blackjack
from game_center import tictactoe

list11 = [1, 2, 3, 4, 6, 7, 8, 9]
brdg = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
brd1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

while True:
    game = input("\nWelcome to Aura's game center!\n1.-Tic Tac Toe\n2.-BalckJack\n3.- Exit\nWhat do you want to play? ")
    if game == "1":
        print("""\nLets play Tic Tac Toe ^.^
Rules:
1.- Computer always starts with an X in the middle 
2.- Choose a number to change the row for an 'O'""")

        brdg[1][1] = "X"
        print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brdg[0][0], ' ' * 7,
              brdg[0][1],
              ' ' * 6, brdg[0][2])
        print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brdg[1][0], ' ' * 7,
              brdg[1][1],
              ' ' * 6, brdg[1][2])
        print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brdg[2][0], ' ' * 7,
              brdg[2][1],
              ' ' * 6, brdg[2][2])
        print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ')
        try:
            while tictactoe.VictoryFor() == True:
                pick = int(input(" Enter your move:  "))
                tictactoe.DisplayBoard(pick)
        except:
            print("""Bad move :( 
             Game over""")
        tictactoe.list1=list11.copy()
        tictactoe.brd=copy.deepcopy(brd1)                           
    if game == "2":
        usercredit = 1000
        bet = 0
        print("\n\nWelcome to Aura's Casino!!")

        print("As a token of our appreciation for choosing us, we are offering $1000 credit!!\n\nAre you ready?\n")
        while True:
            user1 = []
            dealer1 = []
            deckuser = []
            deckdealer = []
            print("\nYour credit: ", usercredit)
            while True:
                bet = input("\n1- $15\n2- $50\n3- $100\n4- $200\nType 'Q' to quit\nChoose your bet: ")
                if bet == "Q":
                    break
                if blackjack.deal(bet) == False:
                    print("Bet does not exist\n")
                else:
                    break
            if bet == "Q":
                break

            usercredit = usercredit - blackjack.deal(bet)
            print("\nYour credit: ", usercredit)
            dealer1.append(blackjack.hit(deckdealer))
            deckdealer.append('--------')
            dealer_hide = deckdealer[:]

            for i in range(2):
                user1.append(blackjack.hit(deckuser))
            blackjack.showhand(deckdealer, deckuser,user1)

            for i in range(2):
                if user1[i] == 1:
                    user1[i] = 11
                    break

            del deckdealer[1]
            dealer1.append(blackjack.hit(deckdealer))

            for i in range(2):
                if dealer1[i] == 1:
                    dealer1[i] = 11
                    break
            while True:
                if sum(user1) == 21 and sum(dealer1) == 21:
                    blackjack.showhand(deckdealer, deckuser,user1)
                    print("\nPush ♻")
                    usercredit = usercredit + blackjack.deal(bet)
                    break
                if sum(user1) == 21:
                    blackjack.showhand(dealer_hide, deckuser,user1)
                    print("\n\n    ♤♡♢♧   ")
                    print("  BlackJack!!   ")
                    print("    ♤♡♢♧   \n\n")
                    print("\n♥ Win ♥")
                    usercredit = usercredit + 2.5 * blackjack.deal(bet)
                    break
                if sum(dealer1) == 21:
                    print("Dealer's Game")
                    blackjack.displaycard(deckdealer)
                    print("\nDealer hits BlackJack ♦ Dealer Wins")
                    break

                bj = input("1.- Hit ☟\n2.- Stand  \n3.- Double \n What do you want to do? ")

                if bj == "1":
                    bj1 = "1"
                    while bj1 == "1":
                        user1.append(blackjack.hit(deckuser))
                        #blackjack.showhand(dealer_hide, deckuser,user1)
                        if sum(user1) > 21:
                            for i in range(2):
                                if user1[i] == 11:
                                    user1[i] = 1
                        for i in range(len(user1)):
                            if user1[i] == 1 and sum(user1) <= 10:
                                user1[i] = 11
                        if sum(user1) > 21:
                            for i in range(len(user1)):
                                if user1[i] == 11:
                                    user1[i] = 1
                        blackjack.showhand(dealer_hide, deckuser,user1)
                        if sum(user1) >= 21:
                            break
                        while True:
                            bj1 = (input("1.- Hit ☟\n2.- Stand ☟\n What do you want to do? "))
                            if bj1 == "2" or bj1 == "1":
                                break

                    if sum(user1) > 21:
                        print("\n♦ Bust ♦")
                        break

                    blackjack.dealergame(dealer1, deckdealer)
                    blackjack.dealerpoints(dealer1)
                    blackjack.showhand(deckdealer, deckuser,user1)
                    usercredit = blackjack.conditions(dealer1, user1, bet, usercredit)
                    break

                if bj == "2":
                    if sum(user1) > 21:
                        print("\n♦ Bust ♦")
                        break
                    blackjack.dealergame(dealer1, deckdealer)
                    blackjack.showhand(deckdealer, deckuser,user1)
                    usercredit = blackjack.conditions(dealer1, user1, bet, usercredit)
                    break

                if bj == "3":
                    usercredit = usercredit - blackjack.deal(bet)

                    user1.append(blackjack.hit(deckuser))
                    if sum(user1) > 21:
                        for i in range(2):
                            if user1[i] == 11:
                                user1[i] = 1
                        for i in range(len(user1)):
                            if user1[i] == 1 and sum(user1) <= 10:
                                user1[i] = 11
                        if sum(user1) > 21:
                            for i in range(len(user1)):
                                if user1[i] == 11:
                                    user1[i] = 1
                    if sum(user1) > 21:
                        blackjack.showhand(deckdealer, deckuser,user1)
                        print("\n♦ Bust ♦")
                        break
                    blackjack.dealergame(dealer1, deckdealer)
                    blackjack.showhand(deckdealer, deckuser,user1)
                    if sum(dealer1) > 21:
                        blackjack.dealerpoints(dealer1)
                        print("\n♥ Win ♥")
                        usercredit = usercredit + 4 * blackjack.deal(bet)
                        break
                    if sum(user1) > sum(dealer1):
                        blackjack.dealerpoints(dealer1)
                        print("\n♥ Win ♥")
                        usercredit = usercredit + 4 * blackjack.deal(bet)
                        break
                    if sum(dealer1) > sum(user1):
                        blackjack.dealerpoints(dealer1)
                        print("\n♢ Dealer Wins ♢")
                        break
                    if sum(dealer1) == sum(user1):
                        blackjack.dealerpoints(dealer1)
                        print("\n♻ Push ♻")
                        usercredit = usercredit + 2 * blackjack.deal(bet)
                        break
            if bet=="Q":
                print("Thank you for playing\nGood bye!")
                break
            if usercredit<=0:
                print("You credit is Over\nThank you for playing\nGood bye!")
                break
    if game=="3":
        print("Good bye!")
        break













