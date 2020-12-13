'''
    I will Create a 2 player, firstly. and Then build and algorithm that would be like the third player.
    (To Play). Players would be ask to choose if they want to play another player or the AI. Players would have to
    answer with a Yes/No to  make a playing choice.

    player would be allow to choose between 2 different characters X or 0 if they are playing another person.
    if the first player make a choice between the 2, the second player is automatically assign the next character.
    Player would enter numbers that would represent the position they which to play.
    Only number 1 - 9 would be use to determine position of play.
'''

'''
    
     A dictionary would be created for the tic tac table.Template for the table would look similar to a mobile phone
     number template where each number in the phone would represent the Tic toc square position. 
     
     Example: 
      1 |  2 | 3  
     ---|----|----
      4 |  5 | 6  
     ---|----|----
      7 |  8 | 9  
        
     
   The Number values would be represented with kay of X or O, depending on what character the players is playing with.
   initial value is empty but would be replaced by a character after each player move. 
   
'''

ticTable = {"1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "}

ticTacKey = []

for key in enumerate(ticTable):
    ticTacKey.append(key)

'''
   Because i would have to print everytime a player make a move, i would create a function that 
   i will call after every move. it would allow me to print when needed. 
'''


def displayTictable(table):
    print(' |', table['1'] + ' | ' + table['2'] + ' | ' + table['3'], '| ')
    print('--------------')
    print(' |', table['4'] + ' | ' + table['5'] + ' | ' + table['6'], '| ')
    print('--------------')
    print(' |', table['7'] + ' | ' + table['8'] + ' | ' + table['9'], '| ')
    print('--------------')


'''
   I build the question code, this would ask question from the player to determine if he/she want to play
   with the AI or not. This are input requested, and what the player decide would determine if player would be 
   playing with AI or human. 
'''
while True:
    docwho = input("Would you like to play with the AI.?: (y/n) ")
    if docwho == "y" or docwho == "Y":
        print("You have chosen to play with the AI")

    elif docwho == "n" or docwho == "N":
        print(" You are playing with human \n")
        char1 = input("Choose between X or 0.? :  ")
        if char1 == "X" or char1 == "x":

            print("You have chosen (x)")
            break
        elif char1 == "o" or char1 == "O":

            print("You have chosen (0)")
            break
        else:
            print("You have not chosen X or O")
            break

    else:
        print("choose if you want to play with the AI or Not")
print("***************************************************************")
# while True:


''' 
    now i would create a function that enter player chosen character in the position they decide base on the table
    number position. I will print out each players play, represented by the character X or 0, in the player chosen
    position. AS mention above the number is a representation of the Tic tac table dictionary, representing Keys
'''


def playGame():
    # I'm using count to determine the number of play turn and if max play turn is reached.
    memmove = char1.upper()
    count = 0

    def onWin():
        displayTictable(ticTable)
        print("Congratulation Player " + memmove + " you have won the game")
        print("Game Over. \n")

    for p in range(10):
        displayTictable(ticTable)
        print("Player, " + memmove + " turn to play.\n Enter 1-9 to take a position")

        '''
        A try catch is added to the input case, in case other characters are entered that are not the specified game
        numbers(string). if this is not abled properly it can break the game flow.'''

        try:
            ursmove = input()

            if ticTable[ursmove] == " ":
                ticTable[ursmove] = memmove
                count += 1
            else:
                print("Position already contain either X or O.\n Play in a blank position")
                if memmove == "O":
                    memmove = "X"
                else:
                    memmove = "O"
        except:
            print("Error has occur")
        finally:
            print("Play")

            # if a player play in a position that is already assign a character the above message
            # notify the player on that.
            '''Because of the limited number of move in the game, a player on only move 4 -5 times to 
                either win the game, lose or draw. so i would build a check to determine if the player X or O
                has won after 5 moves.            
            '''

        if count >= 5:
            if ticTable["1"] == ticTable["2"] == ticTable["3"] != " ":
                # Determine if the character is same on top across table
                onWin()
                break
            elif ticTable["4"] == ticTable["5"] == ticTable["6"] != " ":
                # Determine if the character is same on the middle across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["7"] == ticTable["8"] == ticTable["9"] != " ":
                # Determine if the character is same on bottom down across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["1"] == ticTable["4"] == ticTable["7"] != " ":
                # Determine if the character is same on left side across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["2"] == ticTable["5"] == ticTable["8"] != " ":
                # Determine if the character is same on the middle line  across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["3"] == ticTable["6"] == ticTable["9"] != " ":
                # Determine if the character is same on right side across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["7"] == ticTable["5"] == ticTable["3"] != " ":
                # Determine if the character is same diagonal across table
                displayTictable(ticTable)
                onWin()
                break
            elif ticTable["1"] == ticTable["5"] == ticTable["9"] != " ":
                # Determine if the character is same diagonal across table
                displayTictable(ticTable)
                onWin()
                break
            '''
             After we determine win, we would now determine if the game is draw, three possible outcome 
             of the game is win, draw and lose. the game is draw if no player x and o are able to line their
             character they are playing in any of the above mention win. becouse the game as to complete to determine
             a draw the turn by player in total would be 9. 
             '''
        if count == 9:
            print("\nIt's a draw game!!!\n")
            print("Game Over.")

            '''
            This is a 2 player def and not the AI, i have to allow the second player to play 
            after the first player.
            '''

        if memmove == "X":
            memmove = "O"
        else:
            memmove = "X"

        ''' This is the end of the 2 player function.
        '''


playGame()