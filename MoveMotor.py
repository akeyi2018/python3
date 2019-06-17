import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMOutputDevice

class PWMMove:
    
    def __init__(self, P1, P2, P3, P4):
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        
        self.forwardLeft = PWMOutputDevice(self.P1, True, 0, 60)
        self.reverseLeft = PWMOutputDevice(self.P2, True, 0, 60)
        self.forwardRight = PWMOutputDevice(self.P3, True, 0, 60)
        self.reverseRight = PWMOutputDevice(self.P4, True, 0, 60)
 
    def allStop(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 0
        self.forwardRight.value = 0
        self.reverseRight.value = 0
 
    def forwardDrive(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0
        self.forwardRight.value = 1.0
        self.reverseRight.value = 0
 
    def reverseDrive(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 0
        self.reverseRight.value = 1.0
	
    def forwardTurnLeft(self):
        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = 0
 
    def forwardTurnRight(self):
        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 0.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = 1.0

if __name__ == '__main__':

    test = PWMMove(19,26,6,13)
    test.forwardDrive()
    sleep(0.5)
    test.allStop()
               


