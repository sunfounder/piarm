from robot_hat import Robot,Servo,PWM
from robot_hat.utils import reset_mcu
from time import sleep

from piarm import PiArm

reset_mcu()
sleep(0.01)

arm = PiArm([1,2,3])
#arm.bucket_init(PWM('P3'))
arm.hanging_clip_init(PWM('P3'))
#arm.electromagnet_init(PWM('P3'))
arm.set_offset([0,0,0])

if __name__ == "__main__":
    #print(arm.current_coord,arm.servo_positions, arm.component_staus)
    while True:
        #arm.set_bucket(-50)
        arm.set_hanging_clip(-50)  		
        #arm.set_electromagnet('on')
        sleep(1)		
        #arm.set_bucket(90)
        arm.set_hanging_clip(90)		
        #arm.set_electromagnet('off')
        sleep(1)		
