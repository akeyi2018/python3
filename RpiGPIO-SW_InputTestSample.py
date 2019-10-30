import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 19 
pin2 = 26

GPIO.setup(pin, GPIO.IN)
GPIO.setup(pin2, GPIO.IN)


while True:
    input_val1 = GPIO.input(pin)
    input_val2 = GPIO.input(pin2)
    #total = input_val1 + input_val2
    if input_val1 == 1:
    #    print("19_1")
        time.sleep(0.25)
    else:
        print("19_0")
        time.sleep(0.25)
    if input_val2 == 1:
    #    print("26_1")
        time.sleep(0.25)
    else:
        print("26_0")
        time.sleep(0.25)
    #if total >= 1:
    #    time.sleep(0.25)
    #    if input_val2 == 1:
    #        print("val2")
    #    if input_val1 == 1:
    #        print("val1")
    #elif input_val2 ==1:
    #    print("2")
    #    time.sleep(0.25)
    #else:
    #    print("0")
    #    time.sleep(0.25)
