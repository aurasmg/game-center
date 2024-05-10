import random
list1 = [1, 2, 3, 4, 6, 7, 8, 9]
brd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("""Lets play Tic Tac Toe ^.^
#    Rules:
#    1.- Computer always starts with an X in the middle 
#    2.- Choose a number to change the row for an 'O'""")

# brd[1][1] = "X"
# print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[0][0], ' ' * 7,
#                  brd[0][1],
#                  ' ' * 6, brd[0][2])
# print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[1][0], ' ' * 7,
#                  brd[1][1],
#                  ' ' * 6, brd[1][2])
# print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[2][0], ' ' * 7,
#                  brd[2][1],
#                  ' ' * 6, brd[2][2])
# print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ')

def EnterMove(pick):
    if pick==5:
        print("You cannot choose 5 buddy")
    elif pick<=3:
        pick = pick- 1
        brd[0][pick] = "O"
    elif pick > 3 and pick <= 6:
        pick = pick - 4
        brd[1][pick] = "O"

    elif pick > 6 and pick <= 9:
        pick = pick- 7
        brd[2][pick] = "O"

def EnterMovedraw(x):
    if x <= 3:
        x = x - 1
        brd[0][x] = "X"
    elif x > 3 and x <= 6:
        x = x - 4
        brd[1][x] = "X"
    elif x > 6 and x <= 9:
        x = x - 7
        brd[2][x] = "X"

def DisplayBoard(pick):
    global list1
    list1.remove(pick)
    x = random.choice(list1)
    list1.remove(x)
    # if board==1:
    brd[1][1] = "X"
    EnterMove(pick)
    EnterMovedraw(x)

    print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[0][0], ' ' * 7,
          brd[0][1],
          ' ' * 6, brd[0][2])
    print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[1][0], ' ' * 7,
          brd[1][1],
          ' ' * 6, brd[1][2])
    print("+", '-' * 4, '+ ', "+", '-' * 4, '+ ', "+", '-' * 4, '+ ', '\n', ' ' * 1, brd[2][0], ' ' * 7,
          brd[2][1],
          ' ' * 6, brd[2][2])
def MakeListOfFreeFields(pick):
    list1=[1,2,3,4,5,6,7,8,9]
    del list1[pick-1]
    return list1

def VictoryFor():
    if len(list1)==8:
        return True
    elif (brd[0][0]=="O" and brd[0][1]=="O" and brd[0][2]=="O") \
        or (brd[0][0]=="O" and brd[1][0]=="O" and brd[2][0]=="O") \
        or (brd[2][0]=="O" and brd[2][1]=="O" and brd[2][2]=="O") \
        or (brd[0][2]=="O" and brd[1][2]=="O" and brd[2][2]=="O"):
        print("""
        
        You won! 
        """)
        return False

    elif (brd[0][0]=="X" and brd[0][1]=="X" and brd[0][2]=="X") \
        or (brd[0][0]=="X" and brd[1][0]=="X" and brd[2][0]=="X") \
        or (brd[2][0]=="X" and brd[2][1]=="X" and brd[2][2]=="X") \
        or (brd[0][2]=="X" and brd[1][2]=="X" and brd[2][2]=="X") \
        or (brd[0][0]=="X" and brd[1][1]=="X" and brd[2][2]=="X") \
        or (brd[1][0]=="X" and brd[1][1]=="X" and brd[1][2]=="X") \
        or (brd[0][2]=="X" and brd[1][1]=="X" and brd[2][0]=="X"):
        print("""
        
        
        Computer won! 
        
        """)
        return False
    elif list1==[]:
        print("\n\n\nNobody Won\n\n")
        return False
    else:
        return True


