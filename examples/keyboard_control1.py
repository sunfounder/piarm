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
arm.bucket_init('P3')
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
    j: open
    l: close
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
    bucket = arm.component_staus

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
        bucket -= 1
        flag = True
    elif key == 'l':
        bucket += 1
        flag = True	

    if flag == True:
        arm.set_angle([alpha,beta,gamma])
        arm.set_bucket(bucket)		
        print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

	
if __name__ == "__main__":

    print(manual)

    while True:
        key = readchar()
        control(key)
        if key == chr(27):
            break		
    
    