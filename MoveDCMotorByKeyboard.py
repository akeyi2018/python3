from pynput import keyboard
from pynput.keyboard import Key, Listener
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMOutputDevice

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

forwardLeft = PWMOutputDevice(19, True, 0, 60)
reverseLeft = PWMOutputDevice(26, True, 0, 60)
 
forwardRight = PWMOutputDevice(6, True, 0, 60)
reverseRight = PWMOutputDevice(13, True, 0, 60)
 
def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0
 
def forwardDrive():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0
 
def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 1.0
def forwardTurnLeft():
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0
	forwardRight.value = 0.0
	reverseRight.value = 0
 
def forwardTurnRight():
	forwardLeft.value = 0.0
	reverseLeft.value = 0.0
	forwardRight.value = 0.0
	reverseRight.value = 1.0

        
def on_press(key):
    global NUM_06_Current
    move_step = 1
    try:
        
        if key.char == "a":
            pass
             
        elif key.char == "w":
            forwardDrive()
            sleep(0.2)
            allStop()
            print("W")
             
        elif key.char == "d":
            pass
        elif key.char == "s":
            reverseDrive()
            sleep(0.2)
            allStop()
        elif key.char == "x":
            allStop()    
        
            
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        print("END")
        allStop()
        return False


with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    
