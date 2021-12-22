from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu
from time import sleep
from robot_hat import TTS
import threading

from piarm import PiArm

reset_mcu()
sleep(0.01)
t = TTS()

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

arm = PiArm([1,2,3])
arm.hanging_clip_init('P3')
arm.set_offset([0,0,0])
arm.speed = 100
game_flag = 0

def control():

    alpha,beta,gamma = arm.servo_positions
    clip = arm.component_staus

    if leftJoystick.read_status() == "up":
        alpha += 1
    elif leftJoystick.read_status() == "down":
        alpha -= 1
    if leftJoystick.read_status() == "left":
        gamma += 1
    elif leftJoystick.read_status() == "right":
        gamma -= 1
    if rightJoystick.read_status() == "up":
        beta += 1
    elif rightJoystick.read_status() == "down":
        beta -= 1
    if leftJoystick.read_status() == "pressed":  	
        clip += 1
    elif rightJoystick.read_status() == "pressed":	
        clip -= 1


    # if key_flag == True:
    arm.set_angle([alpha,beta,gamma])
    arm.set_hanging_clip(clip)
        # print('coord: %s , servo angles: %s , clip angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))

def timing():
    sleep(60)
    t.say("three")
    sleep(1)
    t.say("two")
    sleep(1)
    t.say("one")	
    sleep(1)
    t.say("game over")	
    global game_flag
    game_flag = 0	

if __name__ == "__main__":

    thread1 = threading.Thread(target = timing)	
    thread1.start()	
    print("Press two joysticks at the same time to start the game")
    
    while True:
        if 	leftJoystick.read_status() == "pressed" and rightJoystick.read_status() == "pressed":
            t.say("timing begins")
            game_flag = 1		
        if game_flag == 1:
            control()
            
	
		