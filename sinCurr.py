import RPi.GPIO as GPIO
import time
import numpy as np
import math

 
 
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]
GPIO.setup(D, GPIO.OUT)

 
 

def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(round(decNumber)))[2:])) + list(bin(round(decNumber)))[2:]))


def lightNumber(number):
    global D
    GPIO.output(D,0)
    leds = num2dac(number)
    for i in range(len(D)):
        if int(leds[i]):
            GPIO.output(D[i],1)


try:
    time = float(input())
    period = 1 / float(input())
    repetitionsNumber = round(time/ period)
    x = np.absolute(np.rint(255*np.sin(np.linspace(0,time,round(time)*500))))
    for currency in x:
        lightNumber(currency)
        time.sleep(period/500)
       
except ValueError:
    print('Ошибка ввода данных')
time.sleep(0.5)
GPIO.output(D,0)
GPIO.cleanup()