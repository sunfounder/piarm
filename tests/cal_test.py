from robot_hat.utils import reset_mcu
from time import sleep

from piarm import PiArm

reset_mcu()
sleep(0.01)

arm = PiArm([1,2,3])



def _cal_test():
    # arm.do_by_coord([-90,80,80])
    # print(arm.current_coord,arm.servo_positions)

    angles = arm.coord2polar([-75,90,80])
    print(angles)
    coord = arm.polar2coord(angles)
    print(coord)

if __name__ == "__main__":
    _cal_test()