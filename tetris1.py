import random
from random import randint



O_BLOCK = [[(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)]]
I_BLOCK = [[(0, 0), (0+1, 0),(0+2, 0), (0+3, 0)], [(0,0), (0, 0+1), (0, 0+2), (0, 0+3)], [(0, 0), (0+1, 0),(0+2, 0), (0+3, 0)],[(0,0), (0, 0+1), (0, 0+2), (0, 0+3)]]
L_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0)], [(0, 0), (0+1, 0), (0+2, 0), (0+2, 0+1)], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0+2)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)]]
J_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0+2)], [(0+2, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0)], [(0, 0), (0, 0+1), (0+1, 0), (0+2, 0)]]
T_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+2, 0), (0+1, 0+1)], [(0+1, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1) ], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0+1)]]
S_BLOCK = [[(0+1, 0), (0, 0+1), (0, 0+2), (0+1, 0+1) ], [(0, 0), (0+1, 0), (0+1, 0+1), (0+2, 0+1)], [(0+1, 0), (0, 0+1), (0, 0+2), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+1, 0+1), (0+2, 0+1)]]
Z_BLOCK = [[(0, 0+1), (0+1, 0+1), (0+1, 0), (0+2, 0)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+1, 0+2)], [(0, 0+1), (0+1, 0+1), (0+1, 0), (0+2, 0)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+1, 0+2)]]

BLOCKS = [O_BLOCK, I_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK]




class Tetris:
    def __init__(self):
        self.height = 12
        self.width = 10
        self.block = random.choice(BLOCKS)[randint(0,3)]
        self.block_position = (0,4)

    def tick(self):
        row, column = self.block_position
        row += 1
        self.block_position = (row, column)

    def move(self, amount):
        row1, column1 = self.block_position
        test(row1, column1,amount, self)
        if test(row1, column1, amount, self) == False:
            column1
        else:
            column1 += amount

        self.block_position = (row1, column1)

def test(row1, column1, amount, game):
    row1, column1 = game.block_position
    for row, column in game.block:
        if (column1+column+amount) == -1:
            return False
        elif (column1+column+amount) == 10:
            return False
    return True

def draw(game):
    rows = []
    for i in range(game.height):
            row = []
            for i in range(game.width):
                row.append('.')
            rows.append(row)
    for row, column in game.block:
        rows[row + game.block_position[0]][column + game.block_position[1]] = 'X'

    for row in rows:
        print("|", end = "")
        for symbol in row: #s0mbol = " " 0 "0"
            print(symbol, end = " ")
        print("|", end = "\n")


def play_game():
    amount = 0
    game = Tetris()
    draw(game)
    while True:
        tah = input("Number: ")
        if tah == "a":
            amount = -1
            game.move(amount)
        elif tah == "d":
            amount = 1
            game.move(amount)
        else:
            tah = int(tah)
            for i in range(tah):
                game.tick()
        draw(game)
