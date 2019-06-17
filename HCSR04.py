import time
import wiringpi as w

class SonicWave:
    # 1,4,15,10
    def __init__(self, TRIG, ECHO, LED_PIN, dist):
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.LED_PIN = LED_PIN
        self.dist = dist
        w.wiringPiSetup()
        w.pinMode(self.TRIG,1)
        w.pinMode(self.ECHO,0)
        w.pinMode(self.LED_PIN,1)

    def reading(self, sensor):
        if sensor ==0:
            w.digitalWrite(self.TRIG,0)    
            time.sleep(0.1)
            w.digitalWrite(self.TRIG,1)
            time.sleep(0.00001)
            w.digitalWrite(self.TRIG,0)
            while w.digitalRead(self.ECHO) == 0:
                soff = time.time()
            while w.digitalRead(self.ECHO) == 1:
                son = time.time()
            timepassed = son - soff
            return timepassed * 17000
        else:
            print ("Incorrect usonic() function varible.")
    def showLED(self, distance):
        if distance < self.dist:
            w.digitalWrite(self.LED_PIN,1)
            return 1
        else:
            w.digitalWrite(self.LED_PIN,0)
            return 0

if __name__ == "__main__":

    sn = SonicWave(1,4,15,10)
    while True:
        dis = sn.reading(0)
        sn.showLED(dis)
    

