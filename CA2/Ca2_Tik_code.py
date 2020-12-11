'''
    I will Create a 2 player, firstly. and Then build and algorithm that would be like the third player.
    (To Play). Players would be ask to choose if they want to play another player or the AI. Players would have to
    answer with a Yes/No to  make a playing choice.
'''

'''
    
     A dictionary would be created for the board. The Template for the board would look similar to a mobile phone
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

for key in ticTable:
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


displayTictable(ticTable)

while True:

        char1 = input("Would you like to be X or 0.? :  ")
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


    # except:
    #      print("Enter either X or O")
    #      continue
    #
    # finally:
    #     print("Thank for chosen")
    # print(char1)
