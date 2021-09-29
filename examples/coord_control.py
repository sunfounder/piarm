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
arm.set_offset([0,0,0])


def _coord_control():
    arm.speed = 100
    flag = False
    x,y,z = arm.current_coord
    buket_angle = arm.component_staus

    if leftJoystick.read_status() == "up":
        x -= 1
        flag = True
    elif leftJoystick.read_status() == "down":
        x+= 1
        flag = True
    if rightJoystick.read_status() == "left":
        y -= 1
        flag = True
    elif rightJoystick.read_status() == "right":
        y += 1
        flag = True
    if leftJoystick.read_status() == "left":
        z -= 1
        flag = True
    elif leftJoystick.read_status() == "right":
        z += 1
        flag = True
    if rightJoystick.read_status() == "up":
        buket_angle -= 1
        flag = True
    elif rightJoystick.read_status() == "down":
        buket_angle += 1
        flag = True

    if flag == True:
        arm.do_by_coord([x,y,z])
        arm.set_bucket(buket_angle)
        print('coord: %s , servo angles: %s , bucket angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))


if __name__ == "__main__":
    print(arm.current_coord,arm.servo_positions, arm.component_staus)
    while True:
        _coord_control()
        sleep(0.01)