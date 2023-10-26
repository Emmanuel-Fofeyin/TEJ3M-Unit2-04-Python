# Copyright(c) 2023 Emmanuel Fofeyin All rights reserved.
# Created by : Emmanuel Fofeyin
# Created on : Oct 2023
# TEJ3M-Unit2-04.py File.

import time
import board
import digitalio

led13 = digitalio.DigitalInOut(board.GP13)
led12 = digitalio.DigitalInOut(board.GP12)
led11 = digitalio.DigitalInOut(board.GP11)
led13.direction = digitalio.Direction.OUTPUT
led12.direction = digitalio.Direction.OUTPUT
led11.direction = digitalio.Direction.OUTPUT

while True:
    #Green
    led13.value = False
    led12.value = False
    led11.value = True
    time.sleep(1)
    #Blue
    led13.value = False
    led12.value = True
    led11.value = False
    time.sleep(1)
    #Red
    led13.value = True
    led12.value = False
    led11.value = False
    time.sleep(1)
    #Pink
    led13.value = True
    led12.value = True
    led11.value = False
    time.sleep(1)
    #White
    led13.value = True
    led12.value = True
    led11.value = True
    time.sleep(1)
