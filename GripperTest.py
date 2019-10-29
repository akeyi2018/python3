from pynput import keyboard
from pynput.keyboard import Key, Listener
import time
import Adafruit_PCA9685

#Robot Arm No.1 ~ No.6
arm_name = ["Gripper"]
arm_list = [16]

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(50)

# Configure min and max servo pulse lengths
servo_min = 200  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
channel=4

#face search initial
arm_def_position = [0]
arm_cul_position = [0]

def ctrl_direct(Motor_num, position):
    pi.set_servo_pulsewidth(Motor_num, position)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(Motor_num, 0)
    time.sleep(0.2)

"""位置セット"""
def SetPos(pos):
    #pulse = 150～650 : 0 ～ 180deg
    pulse = (650-150)*pos/180+150
    print(pulse)
    pwm.set_pwm(channel,0,int(pulse))
    
def setup():
    print("preparing...")
    for i in range(len(arm_list)):
        ctrl_direct(arm_list[i], arm_def_position[i])
    print("prepare is ready")

def speed(angle, currentval):
    val = abs(angle - currentval)
    if val > 900:
        times = 100
    elif val > 90:
        times = 10
    else:
        times = 1
    if (angle > currentval):
        step = 1*times
    else:
        step = -1*times
    return step

def move_Motor(arm_num, angle, speed):
    for i in range(arm_cul_position[arm_num], angle+speed, speed):
        pi.set_servo_pulsewidth(arm_list[arm_num], i)
        time.sleep(0.02)
    pi.set_servo_pulsewidth(arm_list[arm_num], 0)
    print(arm_name[arm_num] + " moved :" + str(arm_cul_position[arm_num]) + "->" + str(angle))

def angle_ctrl(arm_num, angle):
    global arm_cul_position
    step = speed(angle, arm_cul_position[arm_num])
    move_Motor(arm_num, angle, step)
    arm_cul_position[arm_num] = angle

def Test01(num):
    a = capture()
    return a.captureTest(num)

def searchStep(step):
    val = abs(step)
    if val > 50:
        times = 10
    else:
        times = 4
    return times
def Test01():

    for i in range(5):
        angle_ctrl(0, 750)

        angle_ctrl(0, 1550)

    
def Test02():
    
    for i in range(1000,1102,2):
        p = Test01(i)
        step = searchStep(p[0])
        print(p[0])
        print(step)
        if p[0] < 30 and p[0] > 0:
            break
        else:
            angle = arm_cul_position[5] -step            
            angle_ctrl(5, angle)
   
    print("***end***")

def MoveSG90(num):
    print("OK SG90")
    pwm.set_pwm(channel,0, num)
    
def OriginalPosition():
    for i in range(5,-1,-1):
        angle_ctrl(i, arm_def_position[i])
    
def print_current_position():
    for i in range(len(arm_name)):
        print(arm_name[i] + "'s current position : " + str(arm_cul_position[i]))
        
def on_press(key):
    global NUM_06_Current
    move_step = 1
    try:
        
        if key.char == "q":
            angle = arm_cul_position[0] + move_step 
            #if (angle > 1800):
             #   angle = 1800
            #angle_ctrl(0, angle)
            #MoveSG90(150)
            print(angle)
            
            SetPos(angle)
            arm_cul_position[0]  = angle
             
        elif key.char == "w":
            angle = arm_cul_position[0] - move_step 
            #if (angle < 750):
             #   angle = 750
            #angle_ctrl(0, angle)
             #MoveSG90(650)
            SetPos(angle)
            arm_cul_position[0]  = angle
             
        elif key.char == "a":
            angle = arm_cul_position[1] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(1, angle)
        elif key.char == "s":
            angle = arm_cul_position[1] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(1, angle)
        elif key.char == "z":
            angle = arm_cul_position[2] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(2, angle)
        elif key.char == "x":
            angle = arm_cul_position[2] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(2, angle)
        elif key.char == "e":
            angle = arm_cul_position[3] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(3, angle)
        elif key.char == "r":
            angle = arm_cul_position[3] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(3, angle)
        elif key.char == "d":
            angle = arm_cul_position[4] + move_step
            if (angle > 2500):
                angle = 2500
            angle_ctrl(4, angle)
        elif key.char == "f":
            angle = arm_cul_position[4] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(4, angle)
        elif key.char == "c":
            angle = arm_cul_position[5] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(5, angle)
        elif key.char == "v":
            angle = arm_cul_position[5] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(5, angle)
        elif key.char == "p":
            print_current_position()
            
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        print_current_position()
        OriginalPosition()
        return False


with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    
