
import random
from colorama import *
import timeit

def check_game():
    
    if game_board [0][0] =='X' and game_board[0][1] =='X' and game_board[0][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [1][0] =='X' and game_board[1][1] =='X' and game_board[1][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [2][0] =='X' and game_board[2][1] =='X' and game_board[2][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [0][0] =='X' and game_board[1][1] =='X' and game_board[2][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [2][0] =='X' and game_board[1][1] =='X' and game_board[1][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [0][0] =='X' and game_board[0][1] =='X' and game_board[0][2] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [0][0] =='X' and game_board[1][0] =='X' and game_board[2][0] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [0][1] =='X' and game_board[1][1] =='X' and game_board[2][1] == 'X':
        print("wins player1✨🎉")
        exit

    elif game_board [0][2] =='X' and game_board[1][2] =='X' and game_board[2][2] == 'X':
        print("wins player1✨🎉")
        exit
    
    # return 
    # break
    # exit()
    elif game_board [1][0] =='O' and game_board[1][1] =='O' and game_board[1][2] == 'O':
        print("wins player2✨🎉")
        exit

    elif game_board [2][0] =='O' and game_board[2][1] =='O' and game_board[2][2] == 'O':
        print("wins player2✨🎉")
        exit

    elif game_board [0][0] =='O' and game_board[1][1] =='O' and game_board[2][2] == 'O':
        print("wins player2✨🎉")
        exit

    elif game_board [2][0] =='O' and game_board[1][1] =='O' and game_board[1][2] == 'O':
        print("wins player2✨🎉")
        exit

    elif game_board [0][0] =='O' and game_board[1][0] =='O' and game_board[2][0] == 'O':
        print("wins player2✨🎉")  
        exit  

    elif game_board [0][1] =='O' and game_board[1][1] =='O' and game_board[2][1] == 'O':
        print("wins player2✨🎉")
        exit

    elif game_board [0][2] =='O' and game_board[1][2] =='O' and game_board[2][2] == 'O':
        print("wins player2✨🎉")
        exit

def show():
    for row in game_board:
        for cell in row:
            print (cell, end="") 
        print()  

game_board = [  ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]

show()
check_game()

while True:
    print("player1 start")
    while True:
        row = int(input("row: "))               
        col = int(input("col: "))

        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col] == '-':
                game_board[row][col] = "X"
                break
            else:
                print("dont nobble😤🤬😠")
        else:
            print("enter correct number 0 1 2 😐")

    show()

    print("player2 start")
    while True:
        row = int(input("row: "))               
        col = int(input("col: "))

        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col] == '-':
                game_board[row][col] = "O"
                break
            else:
                print("dont nobble😤🤬😠")
        else:
            print("enter correct number 0 1  2 😐")

    show()
    check_game()






