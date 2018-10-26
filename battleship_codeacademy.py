#!/usr/bin/env python

print "Let's play BATTLESHIP!"

# calling different libraries
from random import randint
import sys


turns = 4

if len(sys.argv) >1:
  try:
      turns = int(sys.argv[1])
  except ValueError:
     pass


# print the board 
board = []

for x in range (0,25):
  board.append(["O"] *25)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

# define randomly the ship position
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# number of  turns for the player to guess the ship position 
  
print "Let\'s start!"

for turn in range(turns):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))-1
  guess_col = int(raw_input("Guess Col: "))-1 

  if guess_row == ship_row and guess_col == ship_col:
     print "Congratulations! You sank my battleship!" 
     break
  else:
    if guess_row not in range(25) or \
      guess_col not in range(25):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn > turns):
      print "Game Over"
    print_board(board)

