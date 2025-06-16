# first project
#blink red lights

from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = True
    time.sleep(.5)
    cp.red_led = False
    time.sleep(.5)
    cp.pixels[0]= (0,100,50)
    time.sleep(.5)
    cp.pixels[0]= (0,0,0)
    time.sleep(.5)
    cp.pixels[1]= (10,20,30)
    time.sleep(.5)
    cp.pixels[1]= (0,0,0)
    time.sleep(.5)


