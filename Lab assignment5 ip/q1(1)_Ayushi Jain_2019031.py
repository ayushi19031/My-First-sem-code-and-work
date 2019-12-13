def who_wins(sequence, x, y):

   """
   Print the winner of a game. Player X
   wins if digit at index x in sequence is
   greater than digit at index y in sequence.
   Player Y wins if digit at index y in
   sequence is greater than digit at index y
   in sequence. Otherwise, nobody wins.
  
   sequence: sequence of digits
   x: index chosen by player X
   y: index chosen by player Y
  
   Precondition:
   sequence is in string format
   x and y are valid integer indices
   """

   x_value = x
   y_value = y  
   if x_value/y_value > 1:
      print("first wins")       
   elif x_value/y_value < 1:
      print("second wins")      
   elif x_value/y_value == 1: 
      print("nobody wins")


who_wins("123123123", 0, 1)