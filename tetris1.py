class Tetris:
    def __init__(self):
        self.height = 12
        self.width = 12
        self.block = [(5,0)]



def draw(game):
    rows = []
    for i in range(game.height):
            row = []
            for i in range(game.width):
                row.append('.')
            rows.append(row)
    for x, y in game.block:
        rows[y][x] = 'X'

    for row in rows:
        print("|", end = "")
        for symbol in row: #symbol = " " x "X"
            print(symbol, end = " ")
        print("|", end = "\n")
game = Tetris()
draw(game)
