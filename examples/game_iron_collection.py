from piarm import PiArm
from robot_hat import Pin,PWM,Servo,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu
from robot_hat import TTS

import threading
import sys
import tty
import termios
import random

reset_mcu()
sleep(0.01)
t = TTS()

arm = PiArm([1,2,3])
arm.electromagnet_init(PWM('P3'))
arm.set_offset([0,0,0])
arm.speed = 100
flag = False



def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

manual1 = '''
Press keys on keyboard
    p: Game Start
    ESC: Stop
'''

manual2 = '''
Press keys on keyboard
    w: extend
    s: retract    
    a: turn left
    d: turn right
    i: go up
    k: go down
    j: on
    l: off
'''

# def control():

#     while flag == True:
#         arm.speed = 100
#         flag = False
#         alpha,beta,gamma = arm.servo_positions

def control(key):
    alpha,beta,gamma = arm.servo_positions	

    if key == 'a':
        gamma += 3		
    elif key == 'd':
        gamma -= 3		
    if key == 's':
        alpha -= 3
    elif key == 'w':
        alpha += 3		
    if key == 'i':
        beta += 3		
    elif key == 'k':
        beta -= 3		
    if key == 'j':
        arm.set_electromagnet('on')		
    elif key == 'l':
        arm.set_electromagnet('off')
    arm.set_angle([alpha,beta,gamma])
        

def timing():
    global flag
    while True:
        if flag == True:
            t.say("game start") 
            sleep(60)
            t.say("three")  
            sleep(1)
            t.say("two")
            sleep(1)
            t.say("one")    
            sleep(1)
            t.say("game over")  
            flag = False

def say_shape():
    k = random.randint(1,3)
    if k == 1:
        t.say("Round")
    if k == 2:
        t.say("Triangle")
    if k == 3:
        t.say("Square") 
    
if __name__ == "__main__":

    print(manual1)

    thread1 = threading.Thread(target = timing) 
    thread1.start()     

    while True:
        key = readchar()
        if  key == 'p':
            print(manual2)
            flag = True
            sleep(3)
            say_shape()
        if flag == True:
            control(key)
        if key == chr(27):
            print("press ctrl+c to quit")
            break	

    
