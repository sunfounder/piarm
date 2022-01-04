Coordinate Control
======================

PiArm's arm has 2 control modes: **Angle Control** and **Coordinate Control**.

* **Angle Control** mode: Write a certain angle to the 3 servos of the arm to make the arm reach a specific position.
* **Coordinate control** mode: Create a spatial coordinate system for the arm, set a control point, and write 3D coordinates to this control point to make the arm reach a specific position.

The **Coordinate Control** mode is used in this project.

Tips on Coordinates of the Arm
-------------------------------------------
PiArm has a space rectangular coordinate system whose origin is located at the center point of the output shaft of the servos on both sides. The control point is located at the top of the arm, and the scale unit is in millimeters. In the initial state, the coordinate of the control point is (0, 80, 80).

.. image:: media/coordinate0.png

It should be noted that the arm length of PiArm is limited, and if the coordinate value is set beyond the limit of its mechanical motion, the PiArm will rotate to an unpredictable Position.

In other words, the total arm length of PiArm is 160mm, which means that the limit value of the control point moving along the Y-axis should ranges from (0,0,0) to (0,160,0). However, due to the limitations of the structure itself, the range of activities should be much smaller than this range.

* The recommended range of X coordinate is -80 ~ 80.
* The recommended range for Y coordinate is 30 ~ 130.
* The recommended range of Z coordinate is 0 ~ 80.

Programming
----------------------------

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 coord_control.py

After the code is run, after the code is run, you will be able to control the rotation of PiArm's Arm by toggling the left and right joystick, and control the angle of the Shovel Bucket by pressing the left and right joystick respectively.

But you need to assemble :ref:`Shovel Bucket` to PiArm first.

**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Servo,PWM,Joystick,ADC,Pin
    from robot_hat.utils import reset_mcu
    from time import sleep

    from piarm import PiArm

    reset_mcu()
    sleep(0.01)

    leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
    rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

    arm = PiArm([1,2,3])
    arm.set_offset([0,0,0])
    arm.bucket_init(PWM('P3'))


    def _coord_control():
        arm.speed = 100
        flag = False
        x,y,z = arm.current_coord
        buket_angle = arm.component_staus

        if leftJoystick.read_status() == "up":
            y += 1
            flag = True
        elif leftJoystick.read_status() == "down":
            y -= 1
            flag = True
        if leftJoystick.read_status() == "left":
            x -= 1
            flag = True
        elif leftJoystick.read_status() == "right":
            x += 1
            flag = True
        if rightJoystick.read_status() == "up":
            z += 1
            flag = True
        elif rightJoystick.read_status() == "down":
            z -= 1
            flag = True

        if leftJoystick.read_status() == "pressed": 	
            buket_angle += 1
            flag = True
        elif rightJoystick.read_status() == "pressed":
            buket_angle -= 1
            flag = True


        if flag == True:
            arm.do_by_coord([x,y,z])
            arm.set_bucket(buket_angle)
            print('coord: %s , bucket angle: %s '%(arm.current_coord,arm.component_staus))

    if __name__ == "__main__":
        while True:
            _coord_control()
            sleep(0.01)


In this code, the function ``_coord_control()`` is created to change the X, Y and Z values of the arm by reading the values of the dual joystick module.

* ``x``, ``y`` and ``z`` refer to the coordinates of the Arm respectively, refer to: :ref:`Tips on Coordinates of the Arm`.
* If the **left** joystick is toggled up, ``y`` increases and the Arm will extend forward.
* If the **left** joystick is toggled down, ``y`` decreases and the Arm will retract backward.
* If the **left** joystick is toggled to the left, ``x`` increases and the Arm will turn left.
* If the **left** joystick is toggled to the right, ``x`` decreases and the Arm will turn right.
* If the **right** joystick is toggled up, ``z`` increases and the Arm will raise up.
* If the **right** joystick is toggled down, ``z`` decreases and the Arm will lower down.
* Finally, use the left and right joystick buttons to control the angle of the Shovel Bucket respectively.


If you have the Hanging Clip or Electromagnet connected to your PiArm, you can modify the above code by referring to the following parts.

* :ref:`clip_joystick`
* :ref:`elec_joystick`