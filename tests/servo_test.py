from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(0.01)

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

d1 = Servo(PWM('P0'))
d2 = Servo(PWM('P1'))
d3= Servo(PWM('P2'))
# d1 = Servo(PWM(1))
# d2 = Servo(PWM(2))
# d3= Servo(PWM(3))
d4 = Servo(PWM('P3'))

d1.angle(0)
d2.angle(0)
d3.angle(0)
d4.angle(0)

angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0

def limit(min,max,x):
    if x > max:
        return max
    elif x < min:
        return min
    else:
        return x

def limit_angle(angles):
    alpha, beta, gamma = angles
    # print([alpha,beta,gamma])
    # limit 
    limit_flag = False

    temp = limit(-30,60,alpha)
    if temp != alpha:
        alpha = temp
        limit_flag = True
    else:
        temp = limit((-alpha-60),(-alpha+30),beta)
        if temp != beta:
            beta = temp
            limit_flag = True
        else:
            temp = limit(-90,40,beta)
            if temp != beta:
                beta = temp
                limit_flag = True

    temp = limit(-90,90,gamma)
    if temp != gamma:
        gamma = temp
        limit_flag = True

    # print(limit_flag,[alpha,beta,gamma])  
    return limit_flag,[alpha,beta,gamma]

def fuc():
    global angle1,angle2,angle3,angle4
    flag = False

    if leftJoystick.read_status() == "up":
        angle1 -= 1
        flag = True
    elif leftJoystick.read_status() == "down":
        angle1 += 1
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

    _,angels = limit_angle([angle1,angle2,angle3])
    angle1,angle2,angle3 = angels

    if flag == True:
        d1.angle(angle1)
        d2.angle(angle2)
        d3.angle(angle3)
        d4.angle(angle4)        
        print(angle1,angle2,angle3,angle4)


if __name__ == "__main__":
    # d2.angle(40)
    while True:
        fuc()
        sleep(0.01)

    # d2.angle(-75)
   
