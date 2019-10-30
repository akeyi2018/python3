import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

#リスト型によるGPIOピンの設定
GPIO.setup(pinList, GPIO.OUT)

#direct->方向の配列；tm->運航時間秒
def FunMoveMotor(direct: list, tm: int):
    
	#Zipを使用することにより従来よりかなり短いプログラムを作成することが可能になる
	for pin, val in zip(pinList, direct):
        GPIO.output(pin, val)

    sleep(tm)


FunMoveMotor(forward, 1)

FunMoveMotor(stop, 0.5)

GPIO.cleanup

print("Finish")
