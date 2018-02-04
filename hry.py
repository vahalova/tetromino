from machine import Pin, PWM, reset
from neopixel import NeoPixel
from time import sleep
pin = Pin(15, Pin.OUT)
pin_up = Pin(0, Pin.IN, Pin.PULL_UP)
pin_down = Pin(13, Pin.IN, Pin.PULL_UP)

POCET_LED = 289
np = NeoPixel(pin, POCET_LED)
def choice_game():
    np = NeoPixel(pin, POCET_LED)
    if pin_up.value()==0:
        for i in range(POCET_LED):
            np[i]=(0,10,30)
        np.write()
        if pin_up.value()!=0:
            import hra_led.py
    elif pin_down.value()==0:
        for i in range(POCET_LED):
            np[i]=(40,10,10)
        np.write()
        if pin_down.value()!=0:
            import hadled.py
for i in range(POCET_LED):
    np[i]=(0,0,0)
np.write()

while True:
    choice_game()
    sleep(0.1)
