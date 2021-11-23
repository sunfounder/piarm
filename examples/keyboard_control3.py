from piarm import PiArm
from robot_hat import Pin,PWM,Servo,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu
from robot_hat import TTS

import sys
import tty
import termios

reset_mcu()
sleep(0.01)
t = TTS()

arm = PiArm([1,2,3])
arm.electromagnet_init('P3')
arm.set_offset([0,0,0])
controllable = 0


manual = '''
Press keys on keyboard to record value!
    W: L_up
    A: L_left
    D: L_right
    S: L_down
    I: R_up
    J: R_left
    K: R_down
    L: R_right
    ESC: Quit
'''

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def control(key):

    arm.speed = 100
    flag = False
    angle1,angle2,angle3 = arm.servo_positions	
    status = ""

    if key == 'a':
        angle3 += 3		
        flag = True
    elif key == 'd':
        angle3 -= 3		
        flag = True
    if key == 'j':
        arm.set_electromagnet('on')		
    elif key == 'l':
        arm.set_electromagnet('off')		
    if key == 's':
        angle1 -= 3
        flag = True
    elif key == 'w':
        angle1 += 3		
        flag = True
    if key == 'i':
        angle2 += 3		
        flag = True
    elif key == 'k':
        angle2 -= 3		
        flag = True
        				
    if flag == True:
        arm.set_angle([angle1,angle2,angle3])	
        print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))

	
if __name__ == "__main__":

    print(manual)

    while True:
        key = readchar()
        control(key)
        if key == chr(27):
            break		
    
    