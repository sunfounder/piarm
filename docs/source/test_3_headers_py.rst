Test 3 Headers
=================

This is the first project to teach us how to control the three head accessories of piarm.

The three accessories correspond to three codes respectively. You need to install the corresponding accessories and then run the corresponding codes.

**Play Shovel Bucket**

.. image:: media/bucket.png

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 shovel.py

After running the code, you will see the shovel keeps working.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.bucket_init('P3')
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:
            arm.set_bucket(-50)
            sleep(1)		
            arm.set_bucket(90)
            sleep(1)

**How it works?**

.. code-block::

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

First, import some modules that need to be used. The robot_hat has been introduced in detail before. The sleep class in the time module is used to control the delay.
The PiArm class in the piarm module encapsulates some founctions based on robot_hat to better control the piarm.

.. code-block::

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.bucket_init('P3')
    arm.set_offset([0,0,0])

Then perform some initialization, among which ``reset_mcu()`` can initialize the robot_hat microcontroller, so that the program can be stable and run from the beginning correctly.

``arm = PiArm([1,2,3])`` create a ``PiArm`` object ``arm`` to control the piarm.

``arm.bucket_init('P3')`` initialize the pin port of the shovel to P3.

``arm.set_offset([0,0,0])`` Zero the rotation angle of the three servos of the piarm.

.. code-block::

    while True:
        arm.set_bucket(-50)
        sleep(1)		
        arm.set_bucket(90)
        sleep(1)

Then you can use the functions encapsulated in the ``PiArm`` class to control the head accessories of the piarm.

``arm.set_bucket()`` are used to control the rotation angle of the shovel servo,



**Play Hanging Clip**

.. image:: media/clip.png

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 clip.py

After running the code, you will see the clip keeps working.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.hanging_clip_init('P3')
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:
            arm.set_hanging_clip(-50)  		
            sleep(1)		
            arm.set_hanging_clip(90)		
            sleep(1)

**How is works?**

``arm.hanging_clip_init('P3')`` initialize the pin port of the clip to P3.

.. code-block::

    while True:
        arm.set_hanging_clip(-50) 
        sleep(1)		
        arm.set_hanging_clip(90)
        sleep(1)

``arm.set_hanging_clip()`` are used to control the rotation angle of the clip servo.

**Play Electromagnet**

.. image:: media/electromagnet.png

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 electromagnet.py

After running the code, You will find that the electromagnet is energized every second (the led light D2 on the electromagnet is on to indicate that it is energized).

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.electromagnet_init('P3')
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:		
            arm.set_electromagnet('on')
            sleep(1)			
            arm.set_electromagnet('off')
            sleep(1)

**How it works?**

``arm.electromagnet_init('P3')`` to initialize the pin port of the electromagnet to P3.

.. code-block::

    while True:
        arm.set_electromagnet('on')
        sleep(1)		
        arm.set_electromagnet('off')
        sleep(1)

``arm.set_electromagnet()`` is used to control whether the electromagnet is energized or not.







