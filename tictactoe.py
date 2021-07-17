# board

board = ["_","_","_",
         "_","_","_",
         "_","_","_",]

# display of the board

def dis_board():
    print (board[0] + " | " + board[1] + " | " + board[2])
    print (board[3] + " | " + board[4] + " | " + board[5])
    print (board[6] + " | " + board[7] + " | " + board[8])

# the_game , player_turn , player_win/tie , index_position 

game_in_progress = True

winner = False

current_player = "X"

def the_game ():

#step 1 : display the dis_board
    dis_board ()

#step 2 : the game should loot until the game falls in a win or a tie
    
    while game_in_progress:
       
        player_turn(current_player)

        final_decision()

        flip_player()

# After the game ends
    if winner == "X" or winner == "O":
        print (winner + " won the match!!")
    elif winner == None:
        print ("The match is a \"TIE\" ladies and gentleman")



# step 3 : position of 

def player_turn(player):    

    print (player + "'s turn")
    indexing_position = input("Enter a value between 1-9:")

    valid = False
    while not valid :
    
        while indexing_position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            indexing_position = input("Enter a value between 1-9:")    
        
        indexing_position = int(indexing_position) - 1

        if board[indexing_position] == "_":
            valid = True
        else :
            print ("You cant go there, try again!!")
    
    board[indexing_position] = player
    dis_board ()
    
def final_decision():
    # 1
    check_for_winner ()
    # 2
    check_if_tie ()

    #1
def check_for_winner():

    global winner

    #rows
    row_winner = check_rows()
    #columns
    column_winner = check_columns()
    #diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #winner
        winner= row_winner 
    elif column_winner:
        #winner
        winner = column_winner 
    elif diagonal_winner:
        #winner
        winner = diagonal_winner 
    else:
        #no winner
        winner = None


    return

def check_rows ():

    global game_in_progress

    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    
    if row1 or row2 or row3:
        game_in_progress = False
    if row1:
        return board[1]
    elif row2:
        return board[4]
    elif row3:
        return board[7]
    
    return

def check_columns ():
    global game_in_progress

    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"
    
    if column1 or column2 or column3:
        game_in_progress = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    
    return

def check_diagonals ():
    global game_in_progress

    diag1 = board[0] == board[4] == board[8] != "_"
    diag2 = board[2] == board[4] == board[6] != "_"
    
    if diag1 or diag2:
        game_in_progress = False
    if diag1:
        return board[8]
    elif diag2:
        return board[6]

    return

def check_if_tie():
    global game_in_progress
    
    if "_" not in board :
        game_in_progress = False
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


the_game ()