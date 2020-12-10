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

print(ticTable)