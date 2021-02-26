from gpiozero import Servo, Button, DistanceSensor
from time import sleep

flg = 0
dis = 0

sensor = DistanceSensor(echo=16, trigger=20)

def openServo():
    servo = Servo(21)
    servo.min()
    sleep(0.2)

def closeServo():
    servo = Servo(21)
    servo.max()
    sleep(0.2)

def setServoState(flg):
    servo = Servo(21)
    if flg == 0:
        servo.min()
    else:
        servo.max()
    sleep(0.2)

closeServo()

while True:
    dis = sensor.distance * 100
    if dis < 10.0:
        openServo()
        sleep(3)
        closeServo()
    sleep(0.5)
