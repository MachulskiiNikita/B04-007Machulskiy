import RPi.GPIO as GPIO
import time
 
 
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]
GPIO.setup(D, GPIO.OUT)



def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(decNumber))[2:])) + list(bin(decNumber))[2:]))


def lightNumber(number):
    global D
    GPIO.output(D,0)
    leds = num2dac(number)
    for i in range(len(D)):
        if int(leds[i]):
            GPIO.output(D[i],1)



try:
    repetitionsNumber = int(input())
    for _ in range(repetitionsNumber):
        for currency in range(256):
            lightNumber(currency)
            time.sleep(0.01)
        for currency in range(255,-1,-1):
                lightNumber(currency)
                time.sleep(0.01)
except ValueError:
    print('Ошибка ввода данных')
GPIO.output(D,0)
GPIO.cleanup()