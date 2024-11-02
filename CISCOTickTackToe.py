#Program to develop a tick-tack-toe game involving 2 players
#Created on 1-11-2024
# SAMPLE INPUT:
#    | |
#  --------
#    | |
#  --------
#    | |
#  --------
#  Your turn player 1
#  Enter your move (1-9):

#SAMPLE OUTPUT:
#   X|O|X
#  --------
#   O|X|
#  --------
#   X|O|X
#  --------
# Congratulations player 1 has won




#Printing the numbering of the board for user reference.
print("The numbering of the board is printed below: ")
print("1|2|3")
print("--------------")
print("4|5|6")
print("--------------")
print("7|8|9")
print("--------------")

#variable containing an empty board
board = [' ']*10

# The function accepts one parameter containing the board's current status
# and prints it out to the console.
def displayboard():  
    row1=  board[0]+'|'+board[1]+'|'+board[2]
    row2=  board[3]+'|'+board[4]+'|'+board[5]
    row3=  board[6]+'|'+board[7]+'|'+board[8]

    print(row1)
    print("--------------")
    print(row2)
    print("--------------")
    print(row3)
    print("--------------")


# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
def enter_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")


#This function checks the whether the horizontal,vertical and diagonal positions have same icons.
#If that is the case player 1 is the winner if the icon is X and player 2 is the winner if the icon is O
def winner(icon):
    if ((board[0] == icon and board[1] == icon and board[2] == icon) or 
       (board[3] == icon and board[4] == icon and board[5] == icon) or 
       (board[6] == icon and board[7] == icon and board[8] == icon) or 
       (board[0] == icon and board[3] == icon and board[6] == icon) or 
       (board[1] == icon and board[4] == icon and board[7] == icon) or 
       (board[2] == icon and board[5] == icon and board[8] == icon) or 
       (board[0] == icon and board[4] == icon and board[8] == icon) or 
       (board[2] == icon and board[4] == icon and board[6] == icon)): 
        return True
    else:
        return False
    
#This function checks whether the spaces in the board are filled or not.
#If all the spaces in the board are filled and no player has won, it will return true else false.
def draw():
    if " " not in board:
        return True
    else:
        return False

#This function gives the user a replay option after finishing the game.
def replay():
    choice=input("Congratulations for playing the game.Want to continue playing? Type yes or no: ")
    return choice =='yes'


#In this loop the entire game is executed using two players
while True:
    #Asking user whether ready to play the game.
    gameon=input("Ready to play the game  .Type y for yes and n for no: ")
    if gameon=='y':
        startgame=True
    else:
        break    
    #Executing the game using icon X for player 1 and icon O for player 2
    while startgame:
        displayboard()
        enter_move("X")
        displayboard()
        if winner("X"):
            print("Congratulations player 1 have won")
            break
        elif draw():
            print("Its a draw")
            break
        enter_move("O")
        if winner("O"):
            displayboard()
            print("Congratulations player 2 have won")
            break
        elif draw():
            print("Its a draw")
            break
    #Discontinuing the game if user dont want to play    
    if not replay():
        break    
