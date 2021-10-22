from piarm import PiArm
from robot_hat import Pin,PWM,Servo,Joystick,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu

import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

manual = '''
Press keys on keyboard to record value!
    W: L_up
    A: L_left
    S: L_right
    D: L_down
    F:record
    I: R_up
    J: R_left
    K: R_rightRR
    L: R_down
    H:reproduce
    ESC: Quit
'''


reset_mcu()
sleep(0.01)


leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

def _coorf_control(key):
    arm.speed = 100
    flag = False
    x,y,z = arm.current_coord
    buket_angle = arm.component_staus

    if leftJoystick.read_status() == "up" or key == 'w':
        x -= 1
        flag = True
    elif leftJoystick.read_status() == "down" or key == 's':
        x+= 1
        flag = True
    if rightJoystick.read_status() == "left" or key == 'j':
        y -= 1
        flag = True
    elif rightJoystick.read_status() == "right" or key == 'l':
        y += 1
        flag = True
    if leftJoystick.read_status() == "left" or key == 'a':
        z -= 1
        flag = True
    elif leftJoystick.read_status() == "right" or key == 'd':
        z += 1
        flag = True
    if rightJoystick.read_status() == "up" or key == 'i':
        buket_angle -= 1
        flag = True
    elif rightJoystick.read_status() == "down" or key == 'k':
        buket_angle += 1
        flag = True

    if flag == True:
        arm.do_by_coord([x,y,z])
        arm.set_bucket(buket_angle)
        # print('coord: %s , servo angles: %s , bucket angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))

def btn_ispresseed(btn_num):
    if btn_num == 0 and leftJoystick.read_status() == "pressed":
        return True
    elif btn_num == 1 and rightJoystick.read_status() == "pressed":   
        return True
    else:
        return False

if __name__ == "__main__":
    arm = PiArm([1,2,3])
    arm.bucket_init('P3')
    arm.set_offset([0,0,0])

    i = 0
    arm.set_speed(100)
    # clear record buffer
    arm.record_buff_clear()

    print(manual)
    while True:
        key = readchar()
        print(key)
        # arm controll by coord
        _coorf_control(key)
        # record buff
        if btn_ispresseed(0) or key == 'f':    
            arm.record()
            print('step %s : %s,%s'%(i,arm.steps_buff[i*2],arm.component_staus))
            i += 1
            sleep(0.05)
        # reproduce steps
        if btn_ispresseed(1) or key == 'h': 
            arm.set_speed(80) 
            arm.record_reproduce(0.05)
            arm.set_speed(100)

        if chr(27) == key:
            break

        sleep(0.01)
    
    