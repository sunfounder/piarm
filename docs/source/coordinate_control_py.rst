Coordinate Control
======================


In addition to the previous method of rotating the axis to control the piarm, we also control the piarm by modifying the coordinate value.

PiArm has a space rectangular coordinate system whose origin is located at the center point of the output shaft of the servos on both sides. The control point is located at the top of the arm, and the scale unit is in millimeters. In the initial state, the coordinate of the control point is (0, 80, 80).

.. image:: media/coordinate0.png

It should be noted that the arm length of PiArm is limited, and if the coordinate value is set beyond the limit of its mechanical motion, the PiArm will rotate to an unpredictable Position.

In other words, the total arm length of PiArm is 160mm, which means that the limit value of the control point moving along the Y-axis should ranges from (0,0,0) to (0,160,0). However, due to the limitations of the structure itself, the range of activities should be much smaller than this range.

.. image:: media/coordinate.png

Therefore, you need to set limits on the range of each coordinate value.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 coord_control.py

After running the code, you can use the joystick to control the piarm.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

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
        if rightJoystick.read_status() == "left":
            buket_angle += 1
            flag = True
        elif rightJoystick.read_status() == "right":
            buket_angle -= 1
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

        if flag == True:
            arm.do_by_coord([x,y,z])
            arm.set_bucket(buket_angle)
            print('coord: %s , bucket angle: %s '%(arm.current_coord,arm.component_staus))

    if __name__ == "__main__":
        while True:
            _coord_control()
            sleep(0.01)

**How it works?**

Angle control is similar to coordinate control. The difference is that the former directly controls the rotation angle of the steering gear, while the latter controls the rotation angle of the steering gear indirectly through algorithm conversion of the control point coordinates.

The PiArm class provides the ``do_by_coord([x,y,z])`` function which allows us to control the piarm using coordinates and call it through the object ``arm``.