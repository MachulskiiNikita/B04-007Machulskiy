import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
D1 = [17]
GPIO.setup(D1, GPIO.OUT)
D = [10,9,11,5,6,13,19,26]
GPIO.setup(D, GPIO.OUT)


class ExitException(Exception):
    def __init__(self, text):
        self.exc = text


def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(round(decNumber)))[2:])) + list(bin(round(decNumber)))[2:]))

def lightNumber(number):
    global D
    GPIO.output(D,0)
    leds = num2dac(number)
    for i in range(len(D)):
        if int(leds[i]):
            GPIO.output(D[i],1)

def currOnComp():
    try:
        GPIO.output(17, 1)
        while True:
            print('Введите число (-1 для выхода):')
            currency = int(input())
            if currency == -1:
                raise ExitException('Произведен выход из программы')
            if currency > 255 or (currency < 0 and currency != -1):
                raise ValueError
            lightNumber(currency)
    except ValueError:
        print('Ошибка ввода данных')
        currOnComp()
    except ExitException as exexc:
        print(exexc)
        GPIO.output([17,10,9,11,5,6,13,19,26], 0)
        GPIO.cleanup()
        return

if __name__ == '__main__':
    currOnComp()
    GPIO.cleanup()