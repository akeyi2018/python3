import time
import wiringpi as w

TRIG = 1
ECHO = 4
LED = 15
    
w.wiringPiSetup()
w.pinMode(TRIG,1)
w.pinMode(ECHO,0)
w.pinMode(LED,1)

distance = 0

def reading(sensor):
    if sensor ==0:
        
        w.digitalWrite(TRIG,0)    
        time.sleep(0.1)
        w.digitalWrite(TRIG,1)
        time.sleep(0.00001)
        w.digitalWrite(TRIG,0)

        while w.digitalRead(ECHO) == 0:
            soff = time.time()
         
        while w.digitalRead(ECHO) == 1:
            son = time.time()

        timepassed = son - soff
        return timepassed * 17000
    
    else:
        print ("Incorrect usonic() function varible.")

while True:
    distance = reading(0)
    if distance < 10:
        w.digitalWrite(LED,1)
    else:
        w.digitalWrite(LED,0)
    #print ("{:0.2f}cm".format(reading(0)))
    #time.sleep(0.1)
