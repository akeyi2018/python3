import webiopi
import pigpio

GPIO = webiopi.GPIO
pi = pigpio.pi()

# ラジコン戦車用パラメータ設定
tank_left_f = 9
tank_left_b = 11
tank_right_f = 23
tank_right_b = 22

def setup():
    # ラジコン戦車用 GPIO ピン設定
    pi.set_mode(tank_right_f, pigpio.OUTPUT)  
    pi.set_mode(tank_right_b, pigpio.OUTPUT)  
    pi.set_mode(tank_left_f, pigpio.OUTPUT)  
    pi.set_mode(tank_left_b, pigpio.OUTPUT)  

def loop():
    webiopi.sleep(0.5)

    # ラジコン戦車用マクロ関数
@webiopi.macro
def tfront():
    #前進
    pi.write(tank_right_f, 1)
    pi.write(tank_right_b, 0)
    pi.write(tank_left_f, 1)
    pi.write(tank_left_b, 0)
  
@webiopi.macro
def tback():
    #後退
    pi.write(tank_right_f, 0)
    pi.write(tank_right_b, 1)
    pi.write(tank_left_f, 0)
    pi.write(tank_left_b, 1)
  
@webiopi.macro
    def tright():
    #右旋回
    pi.write(tank_right_f, 0)
    pi.write(tank_right_b, 1)
    pi.write(tank_left_f, 1)
    pi.write(tank_left_b, 0)
  
@webiopi.macro
    def tleft():
    #左旋回
    pi.write(tank_right_f, 1)
    pi.write(tank_right_b, 0)
    pi.write(tank_left_f, 0)
    pi.write(tank_left_b, 1)
  
@webiopi.macro
    def tstop():
    #停止
    pi.write(tank_right_f, 1)
    pi.write(tank_right_b, 1)
    pi.write(tank_left_f, 1)
    pi.write(tank_left_b, 1)
      
