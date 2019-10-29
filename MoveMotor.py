import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

GPIO.setup(pinList, GPIO.OUT)

def FunMoveMotor(direct, tm):
    for pin, val in zip(pinList, direct):
        GPIO.output(pin, val)
    time.sleep(tm)

def TrunCarLeft(direct):
    for pin, val in zip(pinList, direct):
        GPIO.output(pin, val)
        time.sleep(0.5)
#    FunMoveMotor(stop,0.1)
#    for pin, val in zip(pinList, turnRight):
#        GPIO.output(pin, val)
#        time.sleep(0.5)
   # FunMoveMotor(stop,0.1)
#FunMoveMotor(forward,2.0)
time.sleep(0.5)

for ct in range(10):
    TrunCarLeft(turnLeft)
   # print(ct)
for ct in range(10):
    TrunCarLeft(turnRight)

#FunMoveMotor(back,2.0)
#FunMoveMotor(stop, 0.5)

GPIO.cleanup
print("Finish")
