

from machine import Pin
#from utime import sleep
import uasyncio


onboard_led = Pin("PA5", Pin.OUT)
onboard_led .off()
pc10_led = Pin("PC10", Pin.OUT)
pc10_led.off()

###############################################################################
################################### blync LED #################################
###############################################################################
async def blync(delay):
    while True:
        try:
            onboard_led.value(not onboard_led.value())
            await uasyncio.sleep_ms(delay) # sleep 1 second

            #if not onboard_led.value():
            #    print("LED off")
            #else:
            #    print("LED on")

        except KeyboardInterrupt:
            break


async def blink_led(delay):
    while True:
        pc10_led.on()
        #print("*LED ON*")
        await uasyncio.sleep_ms(delay)

        pc10_led.off()
        #print("*LED OFF*")
        await uasyncio.sleep_ms(delay)


#uasyncio.run(blink_led())



async def main():
    #task = uasyncio.create_task(blync(1000))
    #task = uasyncio.create_task(blink_led(1000))
    task = uasyncio.gather(blink_led(125), blync(1000))
    await task


uasyncio.run(main())
#blync(0.5)
#print("LED starts flashing...")
#onboard_led.off()
#print("Finis!")