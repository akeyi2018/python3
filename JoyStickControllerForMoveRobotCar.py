import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMOutputDevice
import pygame
from pygame.locals import *


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

forwardLeft = PWMOutputDevice(19, True, 0, 100)
reverseLeft = PWMOutputDevice(26, True, 0, 100)
 
forwardRight = PWMOutputDevice(6, True, 0, 100)
reverseRight = PWMOutputDevice(13, True, 0, 100)
 
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

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ('joystick start')

    pygame.init()

    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))
                if e.button == 0:
                    forwardDrive()
                    sleep(0.5)
                    allStop()
                elif e.button == 2:
                    reverseDrive()
                    sleep(0.5)
                    allStop()
                elif e.button == 4:
                    forwardTurnLeft()
                    sleep(0.5)
                    allStop()
                elif e.button == 1:
                    return
        sleep(0.1)

main()

"""
if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ('joystickが見つかりませんでした。')
""" 
