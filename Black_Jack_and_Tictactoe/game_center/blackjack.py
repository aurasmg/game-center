import random
deck=['-  A♠  -','-  2♠  -','-  3♠  -','-  4♠  -','-  5♠  -','-  6♠  -','-  7♠  -','-  8♠  -','-  9♠  -','-  10♠  -','-  J♠  -','-  Q♠  -','-  K♠  -',
      '-  A♥  -','-  2♥  -','-  3♥  -','-  4♥  -','-  5♥  -','-  6♥  -','-  7♥  -','-  8♥  -','-  9♥  -','-  10♥  -','-  J♥  -','-  Q♥  -','-  K♥  -',
      '-  A♦  -','-  2♦  -','-  3♦  -','-  4♦  -','-  5♦  -','-  6♦  -','-  7♦  -','-  8♦  -','-  9♦  -','-  10♦  -','-  j♦  -','-  Q♦  -','-  K♦  -',
      '-  A♣  -','-  2♣  -','-  3♣  -','-  4♣  -','-  5♣  -','-  6♣  -','-  7♣  -','-  8♣  -','-  9♣  -','-  10♣  -','-  j♣  -','-  Q♣  -','-  K♣  -']

suma=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
deck1=deck.copy()
suma1=suma.copy()

def deal(bet):
    if bet=='1':
        bet=15
    elif bet == '2':
        bet = 50
    elif bet=='3':
        bet=100
    elif bet=='4':
        bet=200
    else:
        bet=False
    return bet

def displaycard(deckfirst):
    list1 = []
    side = '--------'
    for i in range(len(deckfirst)):
        list1.append(side)

    data = [list1, list1, deckfirst, list1, list1]

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print("".join(word.ljust(col_width) for word in row))
    list1 = []

def hit(deckcards):
    global deck,suma, suma1, deck1
    if deck==[]:
        deck=deck1.copy()
    if suma==[]:
        suma=suma1.copy()
    mv = random.choice(deck)
    y = deck.index(mv)
    points=suma[y]
    del suma[y]
    deckcards.append(mv)
    deck.remove(mv)
    return points

def showhand(dealer,user,user1):
    print("\n♢ Dealer's game ♤")
    displaycard(dealer)
    print("\n♣ Your Game ♥")
    displaycard(user)
    print("Points:", sum(user1))

def dealergame(dealer1,deckdealer):
    while True:
        if sum(dealer1) == 21:
            return
        if sum(dealer1) > 21:
            for i in range(2):
                if dealer1[i] == 11:
                    dealer1[i] = 1
        for i in range(len(dealer1)):
            if dealer1[i] == 1 and sum(dealer1) <= 10:
                dealer1[i] = 11
        if sum(dealer1) > 21:
            for i in range(len(dealer1)):
                if dealer1[i] == 11:
                    dealer1[i] = 1
        if sum(dealer1) >= 17:
            return
        dealer1.append(hit(deckdealer))

def conditions(dealer1,user1,bet,usercredit):
    if sum(dealer1) > 21:
        print("Dealer's Points: ",sum(dealer1))
        print("\n♥ Win ♥")
        usercredit = usercredit + 2 * deal(bet)
        return usercredit
    if sum(user1) > sum(dealer1):
        print("Dealer's Points: ",sum(dealer1))
        print("\n♥ Win ♥")
        usercredit = usercredit + 2 * deal(bet)
        return usercredit
    if sum(dealer1) > sum(user1):
        print("Dealer's Points: ",sum(dealer1))
        print("\n♢ Dealer Wins ♢")
        return usercredit
    if sum(dealer1) == sum(user1):
        print("Dealer's Points: ",sum(dealer1))
        print("\n♻ Push ♻")
        usercredit = usercredit + deal(bet)
        return usercredit
def dealerpoints(dealer1):
    print("Dealer's Points: ",sum(dealer1))
