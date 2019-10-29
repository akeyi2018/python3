import webiopi

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

g_active = 5

def setup():
    GPIO.setFunction(pinList[0], GPIO.OUT )
    GPIO.setFunction(pinList[1], GPIO.OUT )
    GPIO.setFunction(pinList[2], GPIO.OUT )
    GPIO.setFunction(pinList[3], GPIO.OUT )

def loop():
    if g_active == 1:
        FunMoveMotor(forward,1)
    if g_active == 2:
        FunMoveMotor(turnLeft,1)
    if g_active == 3:
        FunMoveMotor(turnRight,1)
    if g_active == 4:
        FunMoveMotor(back,1)
    if g_active == 5:
        FunMoveMotor(stop,0.5)
    webiopi.sleep(0.5)  
    
def FunMoveMotor(direct, tm):
    for pin, val in zip(pinList, direct):
        GPIO.digitalWrite(pin, val)
    webiopi.sleep(tm)

def forwardDrive(val):
    GPIO.digitalWrite(LED1PIN, val)
    webiopi.sleep(1)
    #GPIO.digitalWrite( LED1PIN, 0 )

@webiopi.macro
def MoveForward(active):
    global g_active
    g_active = int(active)
    return active


    

