import wiringpi as w
import time

pin = 19
w.wiringPiSetup()
w.pinMode(pin,0)


while True:
    if w.digitalRead(pin) == 1:
    #w.digitalWrite(pin,1)
        print("OK")
        time.sleep(0.25)
    else:
    #w.digitalWrite(pin,0)
        print("NG")
        time.sleep(0.25)
        
        
