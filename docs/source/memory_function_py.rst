Memory Function
===================

Piarm provides a function of recording actions, which can be used to record and repeat actions that piarm has done.

In this project, we plan to use the joystick to control the piarm, and record the movement trajectory of the piarm through the joystick buttons, so that the piarm can repeat the previous trajectory movement.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 memory_function.py

After running the code, use the joystick to control the piarm, press the left button of the joystick to record the current action of the piarm (rotation angle of each servo), you can record multiple groups, press the right button of the joystick, and the piarm will replay the recorded action.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python 

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
    arm.set_offset([0,0,0])

    def _angles_control():
        arm.speed = 100
        flag = False
        angle1,angle2,angle3 = arm.servo_positions
        global i	

        if leftJoystick.read_status() == "up":
            angle1 += 1
            flag = True
        elif leftJoystick.read_status() == "down":
            angle1 -= 1
            flag = True
        if leftJoystick.read_status() == "pressed":  	
            arm.record()
            print('step %s : %s,%s'%(i,arm.steps_buff[i*2],arm.component_staus))
            i += 1
            sleep(0.05)
        elif rightJoystick.read_status() == "pressed":	
            arm.set_speed(80) 
            arm.record_reproduce(0.05)
            arm.set_speed(100)
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
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

    if __name__ == "__main__":
        print(arm.servo_positions, arm.component_staus)
        i = 0	
        while True:	
            _angles_control()
            sleep(0.01)

**How it works?**

To reuse the joystick control code, we only need to change the logic of pressing the left and right buttons of the joystick.

.. code-block::

    if leftJoystick.read_status() == "pressed":  	
        arm.record()
        print('step %s : %s,%s'%(i,arm.steps_buff[i*2],arm.component_staus))
        i += 1
        sleep(0.05)
    elif rightJoystick.read_status() == "pressed":	
        arm.set_speed(80) 
        arm.record_reproduce(0.05)
        arm.set_speed(100)    

The PiArm class provides two functions ``record()`` and ``record_reproduce()`` to realize the memory function of the piarm. The former is used to record the current rotation angle of each servo, and the latter is used for the playback of the piarm and can receive parameters
to set the interval time of each action.



