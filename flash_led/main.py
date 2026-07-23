

from machine import Pin
import time


pin_47_led = Pin(47, Pin.OUT)
pin_47_led.off()


while True:
    pin_47_led.on()
    time.sleep(0.25)
    pin_47_led.off()
    time.sleep(0.25)


