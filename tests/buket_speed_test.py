from piarm import PiArm
from robot_hat import Robot,Pin,PWM,Servo,Joystick,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu

reset_mcu()
sleep(0.01)

if __name__ == "__main__":
    bk = Robot([4,5,6],3)
    bk.set_offset([0,0,0])


    bk.servo_move([40,0,0], 100)