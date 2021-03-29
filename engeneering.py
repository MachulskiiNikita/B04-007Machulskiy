import RPi.GPIO as GPIO
import time
 
 
 
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]
GPIO.setup(D, GPIO.OUT)
 
 
 
def lightUp(ledNumber, period):
    global D
    GPIO.output(D,0)
    GPIO.output(D[ledNumber],1)
    time.sleep(period)
    GPIO.output(D[ledNumber],0)
 
 
def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        
def runningLight(count, period):
    global D
    GPIO.output(D,0)
    for k in range(count):
        for i in D:
            GPIO.output(i,1)
            time.sleep(period)
            GPIO.output(i,0)
            
def runningDark(count,period):
    global D
    GPIO.output(D,1)
    for k in range(count):
        for i in D:
            GPIO.output(i,0)
            time.sleep(period)
            GPIO.output(i,1)
    GPIO.output(D,0)
    
    
def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(decNumber))[2:])) + list(bin(decNumber))[2:]))
          
def lightNumber(number):
    global D
    GPIO.output(D,0)
    leds = num2dac(number)
    for i in range(len(D)):
        if int(leds[i]):
            GPIO.output(D[i],1)
 
 
def runningPattern(pattern, direction):
    global D
    GPIO.output(D,0)
    leds = num2dac(pattern)
    for i in range(len(D)):
        if int(leds[i]):
            GPIO.output(D[i],1)
    time.sleep(1)
    GPIO.output(D,0)
    if direction == 'r':
        leds = leds[1:]+[leds[0]]
        for i in range(len(D)):
            if int(leds[i]):
                GPIO.output(D[i],1)
    elif direction == 'l':
        leds = [leds[-1]]+leds[:-1]
        for i in range(len(D)):
            if int(leds[i]):
                GPIO.output(D[i],1)
runningLight(1,0.3)