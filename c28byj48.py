#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

class C28BYJ48:
    """コンストラクタ"""
    def __init__(self, IN1, IN2, IN3, IN4):
        #Setting GPIO
        GPIO.setmode(GPIO.BCM)
        self.mPin = [IN1, IN2, IN3, IN4]     #GPIO Number
        for pin in range(0, 4):
            GPIO.setup(self.mPin[pin], GPIO.OUT)

        #Setting related Sequence
        #1step angle = 1/4096[deg]
        self.mNSeq = 0      #Sequence number from 0 to 7
        self.mSeq = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

        #default speed = max speed
        self.SetWaitTime(0.001)

    """ピンのHigh or Lowを設定する"""
    def SetPinsVoltage(self, NSeq):
        self.mNSeq = NSeq
        for pin in range(0, 4):
            if self.mSeq[self.mNSeq][pin]!=0:
                GPIO.output(self.mPin[pin],GPIO.HIGH)
            else:
                GPIO.output(self.mPin[pin],GPIO.LOW)

    """ウエイト時間を設定する"""
    def SetWaitTime(self, wait):
        if wait < 0.001:
            self.mStep_wait = 0.001
        elif wait > 0.1:
            self.mStep_wait = 0.1
        else:
            self.mStep_wait = wait

    """CWに1Step移動する"""
    def Step_CW(self, step, wait):
        self.SetWaitTime(wait)
        for i in range(0, step):
            if self.mNSeq >= 7:
                self.SetPinsVoltage(0)
            else:
                self.SetPinsVoltage(self.mNSeq+1)
            sleep(self.mStep_wait)

    """CCWに1Step移動する"""
    def Step_CCW(self, step, wait):
        self.SetWaitTime(wait)
        for i in range(0, step):
            if self.mNSeq <= 0:
                self.SetPinsVoltage(7)
            else:
                self.SetPinsVoltage(self.mNSeq-1)
            sleep(self.mStep_wait)

    """終了処理"""
    def Cleanup(self):
        GPIO.cleanup()

"""メイン関数"""
if __name__ == '__main__':
    StepMoter = C28BYJ48(IN1=4, IN2=17, IN3=27, IN4=22)
    #Main loop
    try:
        while True:
            StepMoter.Step_CW(4096,0.001)
            sleep(0.5)
            StepMoter.Step_CCW(4096,0.001)
            sleep(0.5)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        StepMoter.Cleanup()
        print("\nexit program")
