

from machine import Pin
from utime import sleep

onboard_led = Pin("PA5", Pin.OUT)


###############################################################################
################################### blync LED #################################
###############################################################################
def blync(delay):
    while True:
        try:
            onboard_led.value(not onboard_led.value())
            sleep(delay) # sleep 1 second

            if not onboard_led.value():
                print("LED off")
            else:
                print("LED on")

        except KeyboardInterrupt:
            break


blync(0.25)
print("LED starts flashing...")
onboard_led.off()
print("Finis!")