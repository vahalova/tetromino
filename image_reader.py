import png

width, height, lines, meta = png.Reader(filename="names.png").asDirect()
for row, line in enumerate(lines):
    for column, num in enumerate(line[1::3]):
        if num == 0:
            print("({},{}),".format(row, column),end = "")
