import time

SIZE = 12

O_BLOCK = [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)]
I_BLOCK = [[(0, 0), (0+1, 0),(0+2, 0), (0+3, 0)],[(0,0-1), (0, 0), (0, 0+1), (0, 0+2)]]
L_BLOCK = [[(0, 0-1), (0, 0), (0, 0+1), (0+1, 0-1)], [(0, 0), (0+1, 0), (0+2, 0), (0, 0+1)], [(0+1, 0-1), (0+1, 0), (0+1, 0+1), (0, 0+1)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)]]
J_BLOCK = [[(0, 0-1), (0, 0), (0, 0+1), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+2, 0), (0, 0-1)], [(0+1, 0-1), (0+1, 0), (0+1, 0+1), (0, 0-1)], [(0, 0), (0, 0-1), (0+1, 0-1), (0+2, 0-1)]]
T_BLOCK = [[(0, 0-1), (0, 0), (0, 0+1), (0+1, 0)], [(0, 0), (0+1, 0), (0+2, 0), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+2, 0), (0+1, 0-1)], [(0+1, 0-1), (0+1, 0), (0+1, 0+1), (0, 0)]]
S_BLOCK = [[(0, 0), (0, 0+1), (0+1, 0), (0+1, 0-1)], [(0, 0), (0+1, 0), (0+1, 0+1), (0+2, 0+1)]]
Z_BLOCK = [[(0, 0+1), (0+1, 0+1), (0+1, 0), (0+2, 0)], [(0, 0-1), (0, 0), (0+1, 0), (0+1, 0+1)]]

BLOCKS = [O_BLOCK, I_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK]




class Tetris:
    def __init__(self):
        self.height = 12
        self.width = 12
        self.block = O_BLOCK
        self.block_position = (0,5)





    def tick(self):
        row, column = self.block_position
        row += 1
        self.block_position = (row, column)






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


    game = Tetris()
    draw(game)
    while True:
        tah = int(input("Number: "))
        for i in range(tah):
            game.tick()
        draw(game)
