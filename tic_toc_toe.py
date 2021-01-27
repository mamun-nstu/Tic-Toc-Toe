from random import randrange

print("""

|********************* Welcome to Tic Toc Toe ********************|
|                                                                 |
|                                                                 |
|                Developed by : Abdullah Al - Mamun               |
|                          Python developer                       |
|                                                                 |
|      Student of: Noakhali Science & Technology University       |
|        Dept of : Information & Communication Enguineering       |
|                                                                 |
|                                                                 |
|*************************** Let's Play **************************|

""")

# ---------------------> Display Board <---------------------

def display_board():
    print("***************************************")
    print("|                                     |")
    print("|   " + board[0] + " | " + board[1] + " | " + board[2] + "           1 | 2 | 3 " + "    | \n" +
          "|   " + board[3] + " | " + board[4] + " | " + board[5] + "           4 | 5 | 6 " + "    | \n" +
          "|   " + board[6] + " | " + board[7] + " | " + board[8] + "           7 | 8 | 9 " + "    |" )
    print("|                                     |")
    print("***************************************")

# --------------------> Player's name <-----------------------

def players_name(name):
    if name == 1:
        name_1 = input("Enter 1st Player's name : ")
        return name_1
    else:
        name_2 = input("Enter 2nd Player's name : ")
        return name_2
    
    
# ----------------------> Swap Players <----------------------

def swap_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1

# ----------------------> Valid pass check <-------------------

def valid_pass_check(pas):
    while True:
        if pas in range(1, 10) and board[pas-1]=="-":   # valid pass condition
            break
        elif pas in range(1, 10) and board[pas-1]!="-": # position is filled
            print("Sorry, choose another possition.")
            pas = int(input("Give the shot again : "))
            continue
        else:
            print("Input not valid. type number (1 to 9)")  # pass input doesn't match the number range
            pas = int(input("Give the shot again : "))
            continue
    return pas
    
# ----------------------> Player pass <------------------------

def player_pass(current_player):    # argument takes current player number which is (1 or 2)
    if current_player == 1:
        print(player_1 + "'s " + "turn.")
        pas = int(input("Give the shot : "))
        pas = valid_pass_check(pas)     # checking if player pass is in range (1 to 9) and position is empty
        board[pas-1] = 'X'
    else:
        print(player_2 + "'s " + "turn.")
        pas = int(input("Give the shot : "))
        pas = valid_pass_check(pas)     # checking if player pass is in range (1 to 9) and position is empty
        board[pas-1] = 'O'

# -----------------------> Check win <-------------------------

def check_win():
    
    ##### rows checking :
    if board[0]==board[1]==board[2]!="-":   # if all board position have the same value & not empty  
        winner_name(0)   # sending board's position number to check it's value
        return True      # changing "win = False" to "win = True"
    elif board[3]==board[4]==board[5]!="-":
        winner_name(3)
        return True
    elif board[6]==board[7]==board[8]!="-":
        winner_name(6)
        return True
    
    ##### columns checking :
    elif board[0]==board[3]==board[6]!="-":
        winner_name(0)
        return True
    elif board[1]==board[4]==board[7]!="-":
        winner_name(1)
        return True
    elif board[2]==board[5]==board[8]!="-":
        winner_name(2)
        return True

    ##### diagonals checking :
    elif board[0]==board[4]==board[8]!="-":
        winner_name(0)
        return True 
    elif board[2]==board[4]==board[6]!="-":
        winner_name(2)
        return True
    
        
# -----------------------> Winner name <-----------------------

def winner_name(num):   # "num" takes the board's position to check it's value
    if board[num]=="X":
        print(">>>>>>>> Congrats " + player_1 + ". You are the winner <<<<<<<<\n")  # displaying winner name
    else:
        print(">>>>>>>> Congrats " + player_2 + ". You are the winner <<<<<<<<\n")  # displaying winner name

# -----------------------> Check Tie <-------------------------

def check_tie(tie):
    if tie == True:
        print(">>>>>>>> Oh no...!!! It's a tie...!! <<<<<<<<\n")    # displaying Tie message


# ------------------------> Play Again <-----------------------

def play_again():
    print("Wanna play another round.....????? \n")
    print("Select from bellow : ")
    print("***** 1 -> Play Again \n***** 0 -> Exit Game \n")
    x = int(input("Selected : "))
    print()
    if x==1:
        board_index = 0
        while board_index <= 8:
            board[board_index] = "-"    # assinging each board position "-" again for a new board
            board_index += 1
        global player_1
        player_1 = players_name(1)  # taking 1st player's name as input again
        global player_2
        player_2 = players_name(2)  # taking 1st player's name as input again
        print()
        play_game()
    else:
        print("Game exited \n")
    

# ------------------------> Game Toss <------------------------
def game_toss():
    print("System is performing the toss : ")
    toss_winner = randrange(2)
    
    if toss_winner == 0:
        print(player_1," has won the toss.\n")
        return 1
    else:
        print(player_2," has won the toss.\n")
        return 2

# ------------------------> Play Game <------------------------
def play_game():
    current_player = game_toss()      # to toss & set current player
    tie = True
    win = False
    display_board()     # initially displaying the game board
    print()
    pass_counter = 1    # counting each pass of the game
    
    while pass_counter <= 9:    # total 9 pass as there are 9 places in game board   
        player_pass(current_player)     # each pass/shot of player
        print()
        display_board()     # displaying game board after each player pass
        print()
        win = check_win()   # checking if it's a win
        if win == True:     
            tie = False     
            break       # breaking out loop wheneever a win is found
        current_player = swap_player(current_player)    # swapping / changing player turn from current player
        pass_counter += 1
        
    check_tie(tie)  # checking a tie
    play_again()    # asking if wanna play again

# -------------------------> Main Code <------------------------

board = [ "-", "-", "-",    # main game board
          "-", "-", "-",
          "-", "-", "-" ]

print("Select from bellow : ") # asking if you are ready to start playing
print("***** 1 -> Start the game \n***** 0 -> Exit Game")

x = int(input("Select now : "))
if x == 1:
    player_1 = players_name(1)  # taking 1st player's name as input
    player_2 = players_name(2)  # taking 2nd player's name as input
    print()
    play_game()     
else:
    print("\nGame exited \n")     
    
#-------------------------> End of Source Coe <------------------






    
