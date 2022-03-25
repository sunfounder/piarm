from re import M
from robot_hat import PWM
from robot_hat.utils import reset_mcu
from time import sleep
from piarm import PiArm

reset_mcu()
sleep(0.01)

" Grab an object from one coordinate to another coordinate"

arm = PiArm([1,2,3])
arm.set_offset([0,0,0])
arm.hanging_clip_init(PWM('P3'))


if __name__ == "__main__":

    start_coord = [-100, 40, 20] # x,y,z
    end_coord = [100, 40, 30] # x,y,z
    

    arm.set_speed(60)
    arm.set_hanging_clip(20)
    arm.do_by_coord(start_coord)
    arm.set_hanging_clip(90)

    start_coord_up = [start_coord[0], start_coord[1], 80]
    arm.do_by_coord(start_coord_up)

    end_coord_up = [end_coord[0], end_coord[1], 80]
    arm.do_by_coord(end_coord_up)

    arm.do_by_coord(end_coord)
    arm.set_hanging_clip(20)
    arm.do_by_coord(end_coord_up)





