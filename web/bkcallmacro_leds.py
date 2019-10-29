import webiopi
import time

GPIO = webiopi.GPIO

LED1PIN = 19
LED2PIN = 26
LED3PIN = 6

g_led1active = 0
g_led2active = 0
g_led3active = 0
g_speed = 50

def setup():
	GPIO.setFunction( LED1PIN, GPIO.OUT )
	GPIO.setFunction( LED2PIN, GPIO.OUT )
	GPIO.setFunction( LED3PIN, GPIO.OUT )

def forwardDrive(val):
    GPIO.digitalWrite(LED1PIN, val)
    time.sleep(1)
    #GPIO.digitalWrite( LED1PIN, 0 )

@webiopi.macro
def MoveForward(active):
        forwardDrive(int(active))
    

@webiopi.macro
def ChangeSpeed( speed ):
	global g_speed
	g_speed = int(speed)
