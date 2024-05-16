#PROGRAM TO DEVELOP A TICK-TACK-TOE GAME
#CREATED ON 14-5-2024
#LAST EDITED:16-5-2024
import random

#STEP 1:Write a function that can print out a board.
def display_board(board):
    print(board[7] +'|'+board[8]+'|'+board[9])
    print('--------------')
    print(board[4] +'|'+board[5]+'|'+board[6])
    print('--------------')
    print(board[1] +'|'+board[2]+'|'+board[3])

#This is the board where contains the markers.
test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


#STEP 2:Writing a function that can take in a player input and assign their marker as 'X' or 'O'.
def player_input():

    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player1:  Choose X or O: ').upper()

    if marker == 'X':

        return('X','O')      
    else:
        return('O','X') 


#STEP 3:To write a function that takes a board list object ,a marker ('X' or 'O'),
#and a desired position(number 1-9)
#and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker


#STEP 4: To write a function that takes in a board and a mark(X and O)and then checks to see 
#if that mark has won.
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #Checking across the top
           (board[4] == mark and board[5] == mark and board[6] == mark) or #across the middle
           (board[1] == mark and board[2] == mark and board[3] == mark) or #across the bottom
           (board[7] == mark and board[4] == mark and board[1] == mark) or #down the middle
           (board[8] == mark and board[5] == mark and board[2] == mark) or #down the middle
           (board[9] == mark and board[6] == mark and board[3] == mark) or #down the right side
           (board[7] == mark and board[5] == mark and board[3] == mark) or #diagonal
           (board[9] == mark and board[5] == mark and board[1] == mark)) #diagonal

win_check(test_board,'O')

#STEP 5:To write a function that uses random module to randomly decide which player goes first.
def choose_first():
    flip=random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
#STEP 6:To write a function that returns a boolean indicating whether a space on board is freely available.
def space_check(board,position):

    return board[position] == ' ' 


#STEP 7:To check the board and return a boolean value.True if full false otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i): #means if there is space available
            return False
    #Board is full if it returns true    
    return True  

#STEP 8:To ask for players next position( number 1-9) and then use the function from STEP 6
#to check whether it is free position .If it is a free position then return the position
#for later use.
def player_choice(board):
    position = 0
#space_check(board,position) is going to check whether space is available.
    while position  not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position:(1-9): "))

    return position  

#STEP 9:To ask  whether the player wants to play again and return a boolean
def replay():
    choice = input("Want to play the game?.Type yes or no: ")

    return choice == 'Yes'  

#STEP 10:Using while loop to keep running the game.
print('Welcome to tick-tack-toe')

while True:

    #Play the game

    #SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X AND O)

    #Setting up the board.
    the_board = [' ']*10
    #Taking the player input(From STEP 2)
    player1_marker , player2_marker = player_input()
    #Choosing which player will go first. choose_first is the flip function from STEP 5.
    turn = choose_first()
    print(turn + 'will go first')
   #Asking from user whether to play the game or not.
    play_game=input("ready to play the game?.Type y or n: ")

    if play_game == 'y':
        game_on = True
    else:
        break

    #GAME PLAY

    while game_on:
        #If Player 1 starts the game
        if turn == 'Player 1':
            #Show the board.(From STEP 1)
            display_board(the_board)
            #choose a position .(From STEP 8)
            position = player_choice(the_board)

            #Place the marker in the position.(From STEP 3)
            place_marker(the_board,player1_marker,position)
            
            #Check if they have won(From STEP 4 )
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON")
                game_on = False #which means the game is no longer active
            else:
                #Used to check whether the board is full.(From STEP 7 )
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'  

            #Or check if there is a tie

            #If there is no tie or no win then next players turn.


        else:
            #If Player 2 starts the game

            #Show the board(From STEP 1)
            display_board(the_board)
            #choose a position.(From STEP 8)
            position = player_choice(the_board)

            #Place the marker in the position.(From STEP 3)
            place_marker(the_board,player2_marker,position)
            
            #Check if they have won(From STEP 4 )
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON")
                game_on = False #which means the game is no longer active
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'  

    if not replay():
        break
    #BREAK OUT OF WHILE LOOP ON REPLAY                












       
