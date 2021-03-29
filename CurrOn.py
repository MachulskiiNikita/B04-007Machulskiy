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


while True:
    try:
        print('Введите число (-1 для выхода):')
        currency = int(input())
        if currency == -1:
            break
        if currency > 255:
            print('Ошибка ввода данных')
        else:
            lightNumber(currency)
    except ValueError:
        print('Ошибка ввода данных')
time.sleep(0.5)
GPIO.output(D,0)
GPIO.cleanup()