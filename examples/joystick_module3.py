
from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu
from time import sleep
from robot_hat import TTS

from piarm import PiArm

reset_mcu()
sleep(0.01)
t = TTS()

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

arm = PiArm([1,2,3])
arm.electromagnet_init('P3')
arm.set_offset([0,0,0])

def _angles_control():
	arm.speed = 100
	flag = False
	angle1,angle2,angle3 = arm.servo_positions
	status = ""
	
	if leftJoystick.read_status() == "up":
		angle1 += 1
		flag = True
	elif leftJoystick.read_status() == "down":
		angle1 -= 1
		flag = True
	if leftJoystick.read_status() == "pressed": 
		arm.set_electromagnet('on')
		status = "electromagnet is on" 	
	elif rightJoystick.read_status() == "pressed":
		arm.set_electromagnet('off')
		status = "electromagnet is off"	                        
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
		print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))

if __name__ == "__main__":
	while True:
		_angles_control()
		sleep(0.01)