from machine import Pin, PWM, reset
from neopixel import NeoPixel
from time import sleep
pin = Pin(15, Pin.OUT)
pin_up = Pin(13, Pin.IN, Pin.PULL_UP)
pin_down = Pin(0, Pin.IN, Pin.PULL_UP)
TEXT = ((1,0),(1,1),(1,2),(1,4),(1,5),(1,6),(1,8),(1,9),(1,10),(2,1),(2,4),(2,9),(3,1),(3,4),(3,5),(3,9),(4,1),(4,4),(4,9),(5,1),(5,4),(5,5),(5,6),(5,9),(7,1),(7,3),(7,6),(7,9),(7,10),(8,1),(8,3),(8,5),(8,7),(8,9),(8,11),(9,1),(9,2),(9,3),(9,5),(9,6),(9,7),(9,9),(9,11),(10,1),(10,3),(10,5),(10,7),(10,9),(10,11),(11,1),(11,3),(11,5),(11,7),(11,9),(11,10))
NUMBER_LED = 289
np = NeoPixel(pin, NUMBER_LED)
def choice_game():
    np = NeoPixel(pin, NUMBER_LED)
    if pin_up.value()==0:
        for i in range(NUMBER_LED):
            np[i]=(0,10,30)
        np.write()
        if pin_up.value()!=0:
            import tetris_led.py
    elif pin_down.value()==0:
        for i in range(NUMBER_LED):
            np[i]=(40,10,10)
        np.write()
        if pin_down.value()!=0:
            import snake_led.py
for column, row in TEXT:
    number_of_led = row + 2 + (11-column)*25
    np[number_of_led]=(0,5,0)
np.write()

while True:
    choice_game()
    sleep(0.1)
