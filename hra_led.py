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

color = (0, 10, 10)


def led_game():
    np = NeoPixel(pin, LED)
    for led_row, led_column in game.get_block_coord():
        number_of_led = led_row + 2 + led_column*25
        np[number_of_led] = color
    for led_row, led_column in game.waste_dict:
        if led_row >= 0 and led_row <12 and led_column >= 0 and led_column <12:
            number_of_led = led_row + 2 + led_column*25
            np[number_of_led] = color
    np.write()


def on_key_press():
    if pin_left.value()==0:
        game.move(-1)
    elif pin_right.value()==0:
        game.move(1)
    elif pin_up.value()==0:
        game.rotate()



while True:
    led_game()
    game.tick()

    for i in range(5):
        on_key_press()
        if  pin_down.value()!=0:
            sleep(0.1)
        led_game()
