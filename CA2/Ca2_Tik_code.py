'''
    I will Create a 2 player, firstly. and Then build and algorithm that would be like the third player.
    (To Play). Players would be ask to choose if they want to play another player or the AI. Players would have to
    answer with a Yes/No to  make a playing choice.

    player would be allow to choose between 2 different characters X or 0. if the first player make a choice
    between the 2, the second player is automatically assign the next character. Player would enter numbers that would
    represent the position they which to play. Only number 1 - 9 would be use to determine position of play.
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
    print(table['1'] + '|' + table['2'] + '|' + table['3'])
    print('-+-+-')
    print(table['4'] + '|' + table['5'] + '|' + table['6'])
    print('-+-+-')
    print(table['7'] + '|' + table['9'] + '|' + table['9'])


'''
   I build the question code, this would ask question from the player to determine if he/she want to play
   with the AI or not. This are input requested, and what the player decide would determine who he/she play with.
   using if else to make decision. 
'''
while True:
    docwho = input("Would you like to play with the AI.?: (y/n) ")
    if docwho == "y" or docwho == "Y":
        print("You have chosen to play with the AI")
        break
    elif docwho == "n" or docwho == "N":
        print("You are not playing with the AI")
        break
    else:
        print("choose if you want to play with the AI or Not")
print("***************************************************************")
while True:

    char1 = input("Choose between X or 0.? :  ")
    if char1 == "X" or char1 == "x":
        char1x = char1
        print("You have chosen (x)")
        break
    elif char1 == "o" or char1 == "O":
        char10 = char1
        print("You have chosen (0)")
        break
    else:
        print("You have not chosen X or O")

''' 
    now i would create a function that enter player chosen character in the position they decide base on the table
    number position. I will print out each players play, represented by the character X or 0, in the player chosen
    position. AS mention above the number is a representation of the Tic tac table dictionary, representing Keys
'''


def playGame():
    # I'm using count to determine the number of play turn and if max play turn is reached.
    memmove = char1
    count = 0

    def onWin():
        displayTictable(ticTable)
        print("Congratulation Player " + memmove + " you have won the game")
        print("Game Over. \n")

    for p in range(10):
        displayTictable(ticTable)
        print("Player, " + memmove + " turn to play")

        urmove = input()

        if ticTable[urmove] == ' ':
            ticTable[urmove] = memmove
            count += 1
        else:
            print("Position already contain either X or O.\n Play in a blank position")
            continue

            # if a player play in a position that is already assign a character the above message
            # notify the player on that.

            '''
                Becouse of the limited number of move in the game, a player on only move 4 -5 times to 
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
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["7"] == ticTable["8"] == ticTable["9"] != " ":
                    # Determine if the character is same on bottom down across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["1"] == ticTable["4"] == ticTable["7"] != " ":
                    # Determine if the character is same on left side across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["2"] == ticTable["5"] == ticTable["8"] != " ":
                    # Determine if the character is same on the middle line  across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["3"] == ticTable["6"] == ticTable["9"] != " ":
                    # Determine if the character is same on right side across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["7"] == ticTable["5"] == ticTable["3"] != " ":
                    # Determine if the character is same diagonal across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. \n")
                    break
                elif ticTable["1"] == ticTable["5"] == ticTable["9"] != " ":
                    # Determine if the character is same diagonal across table
                    displayTictable(ticTable)
                    print("Congratulation Player " + memmove + " you have won the game \n")
                    print("Game Over. ")
                    break