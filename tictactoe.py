#!/usr/bin/env python3

# display of the board
def dis_board(board):
    for i in range(3,10, 3):
         print(" | ".join(board[i-3:i]))

# verify is there's a connect 3
def verify(board) -> bool:
    return ((board[0] != '_' and board[0] == board[1] == board[2]) or
            (board[3] != '_' and board[3] == board[4] == board[5]) or
            (board[6] != '_' and board[6] == board[7] == board[8]) or
            (board[0] != '_' and board[0] == board[3] == board[6]) or
            (board[1] != '_' and board[1] == board[4] == board[7]) or
            (board[2] != '_' and board[2] == board[5] == board[8]) or
            (board[0] != '_' and board[0] == board[4] == board[8]) or
            (board[2] != '_' and board[2] == board[4] == board[6]))

def flip_player(current_player):
    if current_player == "X":
        return "O" 
    elif current_player == "O":
        return "X"

def player_turn(board):    
    try:
        index = int(input("Enter a value between 1-9: ")) - 1
        while not 0 <= index <= 8 or board[index] != "_":
            index = int(input("Enter a value between 1-9: ")) - 1
    except:
        print("not a valid type.")
    return index

def the_game():
    board = ["_","_","_",
            "_","_","_",
            "_","_","_"]

    current_player = "X"
    dis_board(board)
    while '_' in board:
        print(f"{current_player}'s turn")
        board[player_turn(board)] = current_player
        dis_board(board)
        if verify(board):
            print(f"{current_player} won!")
            return 
        current_player = flip_player(current_player)
    print("tie :(")

the_game()
