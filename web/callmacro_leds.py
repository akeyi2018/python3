import webiopi
import time

webiopi.setDebug()

GPIO = webiopi.GPIO

LED1PIN = 19
LED2PIN = 26
LED3PIN = 6

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

g_led1active = 0
g_led2active = 0
g_led3active = 0
g_speed = 50

def setup():
        GPIO.setFunction(19, GPIO.OUT )
        GPIO.setFunction(26, GPIO.OUT )
        GPIO.setFunction(6, GPIO.OUT )
        GPIO.setFunction(13, GPIO.OUT )

def FunMoveMotor(direct, tm):
    
        GPIO.digitalWrite(pinList[0], direct[0])
        GPIO.digitalWrite(pinList[1], direct[1])
        GPIO.digitalWrite(pinList[2], direct[2])
        GPIO.digitalWrite(pinList[3], direct[3])
        
        time.sleep(tm)

        

def forwardDrive(val):
    GPIO.digitalWrite(LED1PIN, val)
    time.sleep(1)
    #GPIO.digitalWrite( LED1PIN, 0 )


@webiopi.macro
def MoveForward(active):
        if active == 1:
                FunMoveMotor(forward,1)
                FunMoveMotor(stop,1)
        if active == 2:
                FunMoveMotor(turnLeft,1)
        if active == 5:
                GPIO.digitalWrite(19, 0)
                GPIO.digitalWrite(26, 0)
                GPIO.digitalWrite(6, 0)
                GPIO.digitalWrite(13, 0)
    



