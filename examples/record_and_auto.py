from piarm import PiArm
from robot_hat import Pin,PWM,Servo,Joystick,ADC
from time import time,sleep
from robot_hat.utils import reset_mcu


reset_mcu()
sleep(0.01)


leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

def _coorf_control():
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

def btn_ispresseed(btn_num):
    if btn_num == 0 and leftJoystick.read_status() == "pressed":
        return True
    elif btn_num == 1 and rightJoystick.read_status() == "pressed":   
        return True
    else:
        return False

if __name__ == "__main__":
    arm = PiArm([1,2,3])
    arm.bucket_init('P3')
    arm.set_offset([0,0,0])

    i = 0
    arm.set_speed(100)
    # clear record buffer
    arm.record_buff_clear()
    while True:
        # arm controll by coord
        _coorf_control()
        # record buff
        if btn_ispresseed(0) and not btn_ispresseed(1):    
            sleep(0.01)  # key debounce
            if btn_ispresseed(0) and not btn_ispresseed(1):  
                arm.record_buff()
                print('step %s : %s,%s'%(i,arm.steps_buff[i*2],arm.component_staus))
                i += 1
                sleep(0.05)
        # save record
        if btn_ispresseed(1) and not btn_ispresseed(0):  
            sleep(0.01)  # key debounce
            if btn_ispresseed(1) and not btn_ispresseed(0):
                arm.record_save('one')
                print('recorded')
        # reproduce steps
        if btn_ispresseed(0) and btn_ispresseed(1): 
            sleep(0.05)  # key debounce
            if btn_ispresseed(0) and btn_ispresseed(1):
                arm.set_speed(50) 
                arm.record_reproduce('one',0.05)
                arm.set_speed(100)

        sleep(0.01)
    
