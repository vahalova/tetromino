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




def led_game():
    np = NeoPixel(pin, LED)
    for led_row, led_column in game.get_block_coord():
        number_of_led = led_row + 2 + led_column*25
        np[number_of_led] = led_color(game.block_color, 15)
    for (led_row, led_column), color in game.waste_dict.items():
        if led_row >= 0 and led_row <12 and led_column >= 0 and led_column <12:
            number_of_led = led_row + 2 + led_column*25
            np[number_of_led] = led_color(color, 20)
    np.write()

def led_color(color, div):
    r,g,b = color
    return r//div, g//div, b//div




def on_key_press():
    if pin_left.value()==0:
        game.move(-1)
    elif pin_right.value()==0:
        game.move(1)
    elif pin_up.value()==0:
        game.rotate()


try:
    while True:
        led_game()
        game.tick()

        for i in range(5):
            on_key_press()
            if  pin_down.value()!=0:
                sleep(0.1)
            led_game()
except ValueError:
    sleep(3)
    reset()
