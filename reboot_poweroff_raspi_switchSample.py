import RPi.GPIO as GPIO
import time
import os

pin19 = 19
pin26 = 26
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin26,GPIO.OUT)
GPIO.output(pin26,GPIO.LOW)
 
button_previous = 1
button_current = 1
brojac = 0
flag_pressed = 0

try:
    GPIO.wait_for_edge(pin19, GPIO.FALLING)
    while True:
        button_current = GPIO.input(pin19)
        flag_pressed = button_previous + button_current
        if (not(flag_pressed)):
            brojac += 1
        else:
            brojac = 0
        if(button_current and (not button_previous)):
            GPIO.output(pin26,GPIO.HIGH)
            os.system("sudo shutdown -r now")
        if((not flag_pressed) and brojac >= 100):
            GPIO.output(pin26,GPIO.HIGH)
            os.system("sudo poweroff")
            break

        button_previous = button_current
        time.sleep(0.03)

except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()
