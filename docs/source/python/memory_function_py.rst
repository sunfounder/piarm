Memory function
===================

PiArm provides a function to record actions, which allows PiArm to do some repetitive actions automatically.

In this project, let's see how to implement this function.

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 memory_function.py

After the code is run, you can use the left and right joystick to control the rotation of PiArm and the Shovel Bucket (But you need to assemble :ref:`shovel` to PiArm first), press the left joystick to record one movement of PiArm, after recording several sets of movements, you can press the right joystick to make PiArm to reproduce these movements.

Only record the changes between points, if the starting point and the end point are the same, and you do many moves in between, but only press once to record, it will go directly from the starting point to the end point, and will not record the middle process.

**Code**


.. raw:: html

    <run></run>

.. code-block:: python 

    from robot_hat import Servo,PWM,Joystick,ADC,Pin
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS
    from time import sleep
    from piarm import PiArm

    t = TTS()
    reset_mcu()
    sleep(0.01)

    leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
    rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

    arm = PiArm([1,2,3])
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])

    def _angles_control():
        arm.speed = 100
        flag = False
        alpha,beta,gamma = arm.servo_positions
        bucket = arm.component_staus
        global i	

        if leftJoystick.read_status() == "up":
            alpha += 1
            flag = True
        elif leftJoystick.read_status() == "down":
            alpha -= 1
            flag = True
        if leftJoystick.read_status() == "left":
            gamma += 1
            flag = True
        elif leftJoystick.read_status() == "right":
            gamma -= 1
            flag = True
        if rightJoystick.read_status() == "up":
            beta += 1
            flag = True
        elif rightJoystick.read_status() == "down":
            beta -= 1
            flag = True
            
        if rightJoystick.read_status() == "left": 	
            bucket += 2
            flag = True
        elif rightJoystick.read_status() == "right":
            bucket -= 2
            flag = True
            
        if leftJoystick.read_status() == "pressed":  	
            arm.record()
            t.say("record")
            print('step %s : %s'%(i,arm.steps_buff[i*2]))
            i += 1
            sleep(0.05)
        elif rightJoystick.read_status() == "pressed":

            t.say("action")
            arm.set_speed(80) 
            arm.record_reproduce(0.05)
            arm.set_speed(100)
            
        if flag == True:
            arm.set_angle([alpha,beta,gamma])
            arm.set_bucket(bucket)
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

    if __name__ == "__main__":
        print(arm.servo_positions)
        i = 0	
        while True:	
            _angles_control()
            sleep(0.01)

**How it works?**


In this code, let's focus on the ``_angles_control()`` function, which is used to read the value of the dual joystick and then perform different operations.

1. control the movement of the Arm

.. code-block:: python

    if leftJoystick.read_status() == "up":
        alpha += 1
        flag = True
    elif leftJoystick.read_status() == "down":
        alpha -= 1
        flag = True
    if leftJoystick.read_status() == "left":
        gamma += 1
        flag = True
    elif leftJoystick.read_status() == "right":
        gamma -= 1
        flag = True
    if rightJoystick.read_status() == "up":
        beta += 1
        flag = True
    elif rightJoystick.read_status() == "down":
        beta -= 1
        flag = True

* ``alpha``, ``beta`` and ``gamma`` refer to the angles of the 3 servos on the Arm respectively, refer to: :ref:`arm_angle`.
* If the **left** joystick is toggled up, ``alpha`` increases and the Arm will extend forward.
* If the **left** joystick is toggled down, ``alpha`` decreases and the Arm will retract backward.
* If the **left** joystick is toggled to the left, ``gamma`` increases and the Arm will turn left.
* If the **left** joystick is toggled to the right, ``gamma`` decreases and the Arm will turn right.
* If the **right** joystick is toggled up, ``beta`` increases and the Arm will raise up.
* If the **right** joystick is toggled down, ``beta`` decreases and the Arm will lower down.


2. Control the angle of the Shovel Bucket

.. code-block:: python

    if rightJoystick.read_status() == "left": 	
        bucket += 2
        flag = True
    elif rightJoystick.read_status() == "right":
        bucket -= 2
        flag = True

* Right joystick toggles to the left to allow the Shovel Bucket to rewind.
* Right joystick toggles to the right to extend the bucket outward.

3. Recording and reproducing actions

.. code-block:: python

    if leftJoystick.read_status() == "pressed":  	
        arm.record()
        t.say("record")
        print('step %s : %s'%(i,arm.steps_buff[i*2]))
        i += 1
        sleep(0.05)
    elif rightJoystick.read_status() == "pressed":

        t.say("action")
        arm.set_speed(80) 
        arm.record_reproduce(0.05)
        arm.set_speed(100)

* If the left joystick is pressed and the ``record()`` function is called to record the action, PiArm will say that it has recorded. The terminal will show the angle and the number of recorded moves at this point.
* If the right joystick is pressed, the ``record_reproduce()`` function is called to reproduce the recorded action, and PiArm will prompt to start doing the action.

4. Write the angles to PiArm

.. code-block:: python

    if flag == True:
        arm.set_angle([alpha,beta,gamma])
        arm.set_bucket(bucket)
        print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

Write the angle of the Arm and the Shovel Bucket to PiArm and have it rotate to those angles.

If you have the Hanging Clip or Electromagnet connected to your PiArm, you can modify the above code by referring to the following parts.

* :ref:`py_clip_joystick`
* :ref:`py_electro_joystick`