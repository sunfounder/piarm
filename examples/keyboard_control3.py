from piarm import PiArm
from robot_hat import Pin,PWM,Servo,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu

import sys
import tty
import termios

reset_mcu()
sleep(0.01)

arm = PiArm([1,2,3])
arm.electromagnet_init('P3')
arm.set_offset([0,0,0])
controllable = 0


manual = '''
Press keys on keyboard
    w: extend
    s: retract    
    a: turn left
    d: turn right
    i: go up
    k: go down
    j: on
    l: off
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
    alpha,beta,gamma = arm.servo_positions	
    status = ""

    if key == 'w':
        alpha += 3
        flag = True
    elif key == 's':
        alpha -= 3		
        flag = True
    if key == 'a':
        gamma += 3		
        flag = True
    elif key == 'd':
        gamma -= 3		
        flag = True	
    if key == 'i':
        beta += 3		
        flag = True
    elif key == 'k':
        beta -= 3		
        flag = True

    if key == 'j':
        arm.set_electromagnet('on')		
    elif key == 'l':
        arm.set_electromagnet('off')
        
    if flag == True:
        arm.set_angle([alpha,beta,gamma])	
        print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))

	
if __name__ == "__main__":

    print(manual)

    while True:
        key = readchar()
        control(key)
        if key == chr(27):
            break		
    
    