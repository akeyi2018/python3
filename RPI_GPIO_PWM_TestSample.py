import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pinList = [19, 26, 6,13] 

GPIO.setup(pinList, GPIO.OUT) 

def MoveLeftMore(tm):
    GPIO.PWM(26, 120)
    
def MoveLeft(pin, tm):
    p4 = GPIO.PWM(pin, 120)
    p4.start(0)
    for dy in range(60,100,10):
        p4.ChangeDutyCycle(dy)
        time.sleep(tm)
    for dy in range(100,60,-10):
        p4.ChangeDutyCycle(dy)
        time.sleep(tm)
    p4.stop() #Stop PWM

MoveLeftMore(0.5)
"""    
MoveLeft(pinList[0], 0.4)
MoveLeft(pinList[1], 0.4)
MoveLeft(pinList[2], 0.4)
MoveLeft(pinList[3], 0.4)
"""
print("OK")
