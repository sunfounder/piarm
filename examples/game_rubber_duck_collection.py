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
controllable = 0

def control():
    while controllable == 1:	
        arm.speed = 100
        flag = False
        angle1,angle2,angle3 = arm.servo_positions
        angle4 = arm.component_staus

        if leftJoystick.read_status() == "up":
            angle1 += 1
            flag = True
        elif leftJoystick.read_status() == "down":
            angle1 -= 1
            flag = True
        if leftJoystick.read_status() == "pressed":  	
            angle4 += 1
            flag = True
        elif rightJoystick.read_status() == "pressed":	
            angle4 -= 1
            flag = True
        if leftJoystick.read_status() == "left":
            angle3 += 1
            flag = True
        elif leftJoystick.read_status() == "right":
            angle3 -= 1
            flag = True
        if rightJoystick.read_status() == "up":
            angle2 += 1
            flag = True
        elif rightJoystick.read_status() == "down":
            angle2 -= 1
            flag = True

        if flag == True:
            arm.set_angle([angle1,angle2,angle3])
            arm.set_hanging_clip(angle4)
            print('coord: %s , servo angles: %s , clip angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))

def timing():
    sleep(60)
    t.say("three")
    sleep(1)
    t.say("two")
    sleep(1)
    t.say("one")	
    sleep(1)
    t.say("game over")	
    global controllable
    controllable = 0	

if __name__ == "__main__":

    thread1 = threading.Thread(target = control)
    thread2 = threading.Thread(target = timing)	
    i = 1
    while i:
        if 	leftJoystick.read_status() == "pressed" and rightJoystick.read_status() == "pressed":
            i = i - 1
            t.say("timing begins")
            controllable = 1
            thread1.start() 			
            thread2.start()	
	
		