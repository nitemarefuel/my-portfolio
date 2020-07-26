from os import system
import time
a1,a2,a3,b1,b2,b3,c1,c2,c3 = 1,2,3,4,5,6,7,8,9
gameover = False
turn = None
turns = 0
winner = None
def printgrid():
    print("{} {} {}".format(a1,a2,a3))
    print("{} {} {}".format(b1,b2,b3))
    print("{} {} {}".format(c1,c2,c3))

def gameover():
    clear()
    printgrid()
    print(winner + " wins!")
    print("Game Over")

def clear():
    _ = system('clear')

def filled()::w
    print("That square is filled")
    time.sleep(1)
while turns <= 9:
    clear()
    printgrid()
    if turns % 2 == 0:
        turn = "o"
    else:
        turn = "x"
    print("It is " + turn + "'s turn")
    square = str(input("pick a square: "))
    if square == "1":
        if type(a1) == int:
            a1 = turn
            turns +=1
        else:
            filled()
    elif square == "2":
        if type(a2) == int:
            a2 = turn
            turns+=1
        else:
            filled()
    elif square == "3":
        if type(a3) == int:
            a3 = turn
            turns+=1
        else:
            filled()
    elif square == "4":
        if type(b1) == int:
            b1 = turn
            turns+=1
        else:
            filled()
    elif square == "5":
        if type(b2) == int:
            b2 = turn
            turns+=1
        else:
            filled()
    elif square == "6":
        if type(b3) == int:
            b3 = turn
            turns+=1
        else:
            filled()
    elif square == "7":
        if type(c1) == int:
            c1 = turn
            turns+=1
        else:
            filled()
    elif square == "8":
        if type(c2) == int:
            c2 = turn
            turns+=1
        else:
            filled()
    elif square == "9":
        if type(c3) == int:
            c3 = turn
            turns+=1
        else:
            filled()
    else:
        print("Not understood")
        time.sleep(1)

    if a1 == a2 == a3 != int:
        winner = a1
        gameover()
        break

    elif b1 == b2 == b3 != int:
        winner = b1
        gameover()
        break
    elif c1 == c2 == c3 != int:
        winner = c1
        gameover()
        break
    elif a1 == b1  == c1 != int:
        winner = a1
        gameover()
        break

    elif a2 == b2 == c2 != int:
        winner = a2
        gameover()
        break

    elif a3 == b3 == c3 != int:
        winner = a3
        gameover()
        break

    elif a1 == b2 == c3 != int:
        winner = a1
        gameover()
        break

    elif a3 == b2 == c1 != int:
        winner = a3
        gameover()
        break
    elif turns == 9:
        winner = "Nobody "
        gameover()
        break

