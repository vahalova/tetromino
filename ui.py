import tetris1

import pyglet
from pyglet import gl


def draw_rectangle(x, y, w, h):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x), int(y))
    gl.glVertex2f(int(x+w), int(y))
    gl.glVertex2f(int(x+w), int(y+h))
    gl.glVertex2f(int(x), int(y+h))
    gl.glEnd()


window = pyglet.window.Window()
game = tetris1.Tetris()

@window.event
def on_draw():
    window.clear()
    tile_width = window.width / game.width
    tile_height = window.height / game.height
    block_coords = set(game.get_block_coord())
    for row in range(game.height):
        for col in range(game.width):
            coords = row, col
            if coords in block_coords:
                color = (20, 0, 0)
            else:
                color = game.waste_dict.get(coords, (0, 0, 0))
            gl.glColor3f(*(min(1, c/20) for c in color))
            draw_rectangle(col * tile_width,
                           window.height - (row+1) * tile_height,
                           tile_width + 1, tile_height + 1)

@window.event
def on_key_press(key, mod):
    if key == pyglet.window.key.LEFT:
        game.move(-1)
    if key == pyglet.window.key.RIGHT:
        game.move(1)
    if key == pyglet.window.key.UP:
        game.rotate()

def tick(dt):
    game.tick()

pyglet.clock.schedule_interval(tick, 1/2)

pyglet.app.run()
