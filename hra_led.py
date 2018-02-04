import tetris1
import time
import os

from machine import Pin, PWM, reset
from neopixel import NeoPixel
from time import sleep

LED = 289
game = tetris1.Tetris()
pin = Pin(15, Pin.OUT)
pin_left = Pin(12, Pin.IN, Pin.PULL_UP)
pin_right = Pin(14, Pin.IN, Pin.PULL_UP)
pin_up = Pin(0, Pin.IN, Pin.PULL_UP)
pin_down = Pin(13, Pin.IN, Pin.PULL_UP)
block_move = game.tick()
color = (0, 10, 10)


def led_game():
    np = NeoPixel(pin, LED)
    for led_row, led_column in game.get_block_coord():
        number_of_led = led_row + 2 + led_column*25
        np[number_of_led] = color
    for led_row, led_column in game.waste_dict:
        if led_row > 0 and led_row <12 and led_column > 0 and led_column <12:
            number_of_led = led_row + 2 + led_column*25
            np[number_of_led] = color
    np.write()

"""


def on_key_press(key, mod):
    global block_move

    if key == pin_left.value()==0:
        game.move(-1)
    if key == pin_right.value()==0:
        game.move(1)
    if pin_up.value()==0:
        game.rotate()
    return block_move

def tick(dt):
    game.tick()
"""

while True:
    led_game()
    game.tick()
    sleep(1)
