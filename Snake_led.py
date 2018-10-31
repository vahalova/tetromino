import time
import os

from machine import Pin, PWM, reset
from neopixel import NeoPixel
from time import sleep

SIZE = 12
NUMBER_LED= 289
ROW = 2
COLUMN = 25
a = SIZE//2
b = SIZE//2
snake = [[a, b], [(a), (b + 1)], [(a), (b + 2)]]
direction = "d"
pin = Pin(15, Pin.OUT)
pin_left = Pin(14, Pin.IN, Pin.PULL_UP)
pin_right = Pin(12, Pin.IN, Pin.PULL_UP)
pin_up = Pin(13, Pin.IN, Pin.PULL_UP)
pin_down = Pin(0, Pin.IN, Pin.PULL_UP)


def randint(a, b):
    return os.urandom(1)[0] % (b-a) + a


o = randint(0, SIZE-1)
k = randint(0, SIZE-1)
food = [[o, k]]


def field(snake_color=(0, 10, 0)):
    np = NeoPixel(pin, NUMBER_LED)
    for x, y in snake:
        led_number = x + ROW + y*COLUMN
        np[led_number] = snake_color
    for x, y in food:
        led_number = x + ROW + y*COLUMN
        np[led_number] = (0, 10, 10)
    if snake[-1] == food[-1]:
        led_number = x + ROW + y*COLUMN
        np[led_number] = (10, 0, 0)
    np.write()


def get_the_answer():
    global direction
    if pin_up.value() == 0:
        direction = "w"
    elif pin_down.value() == 0:
        direction = "s"
    elif pin_left.value() == 0:
        direction = "a"
    elif pin_right.value() == 0:
        direction = "d"
    return direction


def move(answer):
    v, b = snake[-1]
    o, k = food[0]
    if answer == "w":
        if v == 0:
            v = (SIZE-1)
        else:
            v -= 1
    elif answer == "a":
        if b == 0:
            b = (SIZE-1)
        else:
            b -= 1
    elif answer == "s":
        if v == (SIZE-1):
            v = 0
        else:
            v += 1
    elif answer == "d":
        if b == (SIZE-1):
            b = 0
        else:
            b += 1

    test_move(v, b)
    if test_move(v, b) == False:
        raise ValueError

    if food[-1] != snake[-1]:
        snake.pop(0)
        snake.append([v, b])
    else:  # When the snake eats the food
        while True:
            """Calculating next food's coordinates"""
            new_food = ([randint(0, SIZE-1), randint(0, SIZE-1)])
            if new_food not in snake:
                break

        food.append(new_food)
        food.pop(0)
        snake.append([v, b])


def test_move(v, b):
    if [v, b] in snake:
        return False
    return True


def game_snake():
    while True:
        field()
        answer = get_the_answer()
        move(answer)
        if food[-1] != snake[-1]:
            pin_buzzer = Pin(5, Pin.OUT)
            pwm = PWM(pin_buzzer, freq=5, duty=1)
        else:
            pin_buzzer = Pin(5, Pin.OUT)
            pwm = PWM(pin_buzzer, freq=55, duty=500)
        for i in range(20):
            get_the_answer()
            sleep(0.01)


try:
    game_snake()


except ValueError:
    field(snake_color=(15, 7, 0))
    pin_buzzer = Pin(5, Pin.OUT)
    pwm = PWM(pin_buzzer, freq=0, duty=0)
    sleep(3)
    reset()
