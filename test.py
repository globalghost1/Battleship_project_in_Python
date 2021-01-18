import Output
import input_bt
import battleship
from colorama import *
from enums import Players

board1 = [['0', '0', '0', '0', '0'],
          ['0', 'X', '0', '0', '0'],
          ['0', '0', 'X', 'X', '0'],
          ['0', '0', '0', '0', '0'],
          ['0', '0', '0', '0', '0']]

board2 = [['0', '0', '0', '0', '0'],
          ['0', '0', '0', '0', '0'],
          ['0', 'M', 'H', 'M', '0'],
          ['0', '0', '0', '0', '0'],
          ['0', '0', '0', '0', '0']]

players = [Players.Player1, Players.Player2]
print(input_bt.ai_shoot(board2))
Output.display_board(board2)
