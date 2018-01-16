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
        self.block = random.choice(BLOCKS)
        self.block_rotation = randint(0,3)
        self.block_position = (0,4)
        self.waste_list = []

    def tick(self):

        row1, column1 = self.block_position
        row1 += 1
        self.block_position = (row1, column1)





    def move(self, amount):
        row1, column1 = self.block_position
        move_test(row1, column1,amount, self)
        if move_test(row1, column1, amount, self) == False:
            column1
        else:
            column1 += amount
        self.block_position = (row1, column1)

    def rotate(self):
        row1, column1 = self.block_position
        self.block_rotation += 1
        if self.block_rotation == 4:
            self.block_rotation = 0
        rotate_test_side(row1, column1, self)
        if rotate_test_side(row1, column1, self) == False:
            column1 -= 3
        rotate_test_bottom(row1, column1, self)
        if rotate_test_bottom(row1, column1, self) == False:
            row1 -=3
        self.block_position = (row1, column1)

    def waste(self):
        row1, column1 = self.block_position
        waste_test(row1, column1, self)
        if waste_test(row1, column1, self) == False:
            for row, column in self.block[self.block_rotation]:
                self.waste_list.append([row+row1, column+column1])
            self.block = random.choice(BLOCKS)
            self.block_rotation = randint(0,3)
            self.block_position = (0,4)

def move_test(row1, column1, amount, game):
    for row, column in game.block[game.block_rotation]:
        if (column1+column+amount) == -1:
            return False
        elif (column1+column+amount) == 10:
            return False
    return True

def waste_test(row1, column1, game):
    for row, column in game.block[game.block_rotation]:
        if (row + row1) == 11:
            return False
        
    return True

def rotate_test_side(row1, column1, game):
    for row, column in game.block[game.block_rotation]:
        if (column1+column) == 11:
            return False
    return True

def rotate_test_bottom(row1, column1, game):
    for row, column in game.block[game.block_rotation]:
        if (row+row1) == 12:
            return False
    return True


def draw(game):
    rows = []
    for i in range(game.height):
            row = []
            for i in range(game.width):
                row.append('.')
            rows.append(row)
    for row, column in game.block[game.block_rotation]:
        rows[row + game.block_position[0]][column + game.block_position[1]] = 'X'
    for row, column in game.waste_list:
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
                game.waste()
        draw(game)
