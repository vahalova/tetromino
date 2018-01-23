import random
from random import randint



O_BLOCK = [[(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)], [(0, 0), (0+1, 0), (0, 0+1), (0+1,0+1)]]
I_BLOCK = [[(0, 0), (0+1, 0),(0+2, 0), (0+3, 0)], [(0,0), (0, 0+1), (0, 0+2), (0, 0+3)], [(0, 0), (0+1, 0),(0+2, 0), (0+3, 0)],[(0,0), (0, 0+1), (0, 0+2), (0, 0+3)]]
L_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0)], [(0, 0), (0+1, 0), (0+2, 0), (0+2, 0+1)], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0+2)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)]]
J_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0+2)], [(0+2, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0)], [(0, 0), (0, 0+1), (0+1, 0), (0+2, 0)]]
T_BLOCK = [[(0, 0), (0, 0+1), (0, 0+2), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+2, 0), (0+1, 0+1)], [(0+1, 0), (0+1, 0+1), (0+1, 0+2), (0, 0+1)], [(0+1, 0), (0, 0+1), (0+1, 0+1), (0+2, 0+1)]]
S_BLOCK = [[(0+1, 0), (0, 0+1), (0, 0+2), (0+1, 0+1) ], [(0, 0), (0+1, 0), (0+1, 0+1), (0+2, 0+1)], [(0+1, 0), (0, 0+1), (0, 0+2), (0+1, 0+1)], [(0, 0), (0+1, 0), (0+1, 0+1), (0+2, 0+1)]]
Z_BLOCK = [[(0, 0+1), (0+1, 0+1), (0+1, 0), (0+2, 0)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+1, 0+2)], [(0, 0+1), (0+1, 0+1), (0+1, 0), (0+2, 0)], [(0, 0), (0, 0+1), (0+1, 0+1), (0+1, 0+2)]]

BLOCKS = [O_BLOCK, I_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK]

COLOR = (0,20,0)


class Tetris:
    def __init__(self):
        self.height = 12
        self.width = 10
        self.block = random.choice(BLOCKS)
        self.block_rotation = randint(0,3)
        self.block_position = (0,4)
        self.waste_dict = {}
        for row in range(self.height):
            self.waste_dict[row, -1] = (0,0,0)
            self.waste_dict[row, self.width] = (0,0,0)
        for column in range(self.width):
            self.waste_dict[self.height, column] = (0,0,0)
    def tick(self):
        row1, column1 = self.block_position

        self.block_position = (row1+1, column1)
        if waste_test(self) == False:
            self.block_position = (row1, column1)
            for row, column in self.get_block_coord():
                self.waste_dict[row, column] = COLOR
            self.block = random.choice(BLOCKS)
            self.block_rotation = randint(0,3)
            self.block_position = (0,4)








    def move(self, amount):
        row1, column1 = self.block_position
        self.block_position = (row1, column1+amount)
        if waste_test(self) == False:
            self.block_position = (row1, column1)


    def rotate(self):
        row1, column1 = self.block_position
        self.block_rotation += 1
        if self.block_rotation == 4:
            self.block_rotation = 0

        self.block_position = (row1, column1)


    def get_block_coord(self):
        result = []
        for block_row, block_column in self.block[self.block_rotation]:
            row = block_row + self.block_position[0]
            column = block_column + self.block_position[1]
            result.append((row,column))
        return result




def waste_test(game):

    for row, column in game.get_block_coord():
        if (row, column) in game.waste_dict:
            return False
    return True








def draw(game):

    rows = []
    for row_num in range(game.height):
            row = []
            for column_num in range(game.width):
                if (row_num, column_num) in game.waste_dict:
                    row.append('X')
                else:
                    row.append('.')
            rows.append(row)
    for row, column in game.get_block_coord():
        print(row, column)
        rows[row][column] = 'X'

    for row in rows:
        print("|", end = "")
        for symbol in row: #symbol = " " x "X"
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
        elif tah =="w":
            game.rotate()

        else:
            tah = int(tah)
            for i in range(tah):
                game.tick()
        draw(game)
