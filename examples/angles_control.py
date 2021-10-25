
from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu
from time import sleep

from piarm import PiArm

reset_mcu()
sleep(0.01)

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

arm = PiArm([1,2,3])
arm.bucket_init('P3')
# arm.hanging_clip('P3')
# arm.electromagnet_init('P3')
arm.set_offset([0,0,0])

def _angles_control():
    arm.speed = 100
    flag = False
    angle1,angle2,angle3 = arm.servo_positions
    angle4 = arm.component_staus

    if leftJoystick.read_status() == "up":
        angle1 -= 1
        flag = True
    elif leftJoystick.read_status() == "down":
        angle1+= 1
        flag = True
    if rightJoystick.read_status() == "left":
        angle2 -= 1
        flag = True
    elif rightJoystick.read_status() == "right":
        angle2 += 1
        flag = True
    if leftJoystick.read_status() == "left":
        angle3 -= 1
        flag = True
    elif leftJoystick.read_status() == "right":
        angle3 += 1
        flag = True
    if rightJoystick.read_status() == "up":
        angle4 -= 1
        flag = True
    elif rightJoystick.read_status() == "down":
        angle4 += 1
        flag = True

    if flag == True:
        arm.set_angle([angle1,angle2,angle3])
        arm.set_bucket(angle4)
        print('coord: %s , servo angles: %s , bucket angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))

if __name__ == "__main__":
    print(arm.servo_positions, arm.component_staus)
    while True:
        _angles_control()
        sleep(0.01)