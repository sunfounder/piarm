from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu
from time import sleep

from piarm import PiArm

reset_mcu()
sleep(0.01)

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

arm = PiArm([1,2,3])
arm.hanging_clip_init('P3')
arm.set_offset([0,0,0])

def _angles_control():
    arm.speed = 100
    flag = False
    alpha,beta,gamma = arm.servo_positions
    clip = arm.component_staus

    if leftJoystick.read_status() == "up":
        alpha += 1
        flag = True
    elif leftJoystick.read_status() == "down":
        alpha -= 1
        flag = True
    if leftJoystick.read_status() == "left":
        gamma += 1
        flag = True
    elif leftJoystick.read_status() == "right":
        gamma -= 1
        flag = True
    if rightJoystick.read_status() == "up":
        beta += 1
        flag = True
    elif rightJoystick.read_status() == "down":
        beta -= 1
        flag = True
        
    if leftJoystick.read_status() == "pressed": 	
        clip += 2
        flag = True
    elif rightJoystick.read_status() == "pressed":	
        clip -= 2
        flag = True

    if flag == True:
        arm.set_angle([alpha,beta,gamma])
        arm.set_hanging_clip(clip)
        print('servo angles: %s , clip angle: %s '%(arm.servo_positions,arm.component_staus))

if __name__ == "__main__":
    while True:
        _angles_control()
        sleep(0.01)