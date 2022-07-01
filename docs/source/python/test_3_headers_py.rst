Test 3 EoATs
=================================================

This is the first program, and the one you must see.

In this program, you will learn how to assemble and use PiArm's 3 end-of-arm tools.

.. _py_shovel:

Shovel Bucket
--------------------------

**Run the code**


.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 shovel.py

After running the code, you will see the Shovel Bucket moving back and forth. But you need to assemble :ref:`shovel` first.

**Code**


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
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:
            arm.set_bucket(-50)
            sleep(1)		
            arm.set_bucket(90)
            sleep(1)

**How it work？**

.. code-block::

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

* First, import the ``Robot``, ``servo``, and ``PWM`` classes from `robot_hat <https://docs.sunfounder.com/projects/robot-hat/en/latest/index.html>`_.
* Import the ``reset_mcu`` class from the ``robot_hat.utils`` module, which is used to reset the MCU, to avoid conflicts between programs that can cause communication errors.
* Import the ``sleep`` class from the ``time`` module, which is used to implement the time delay function in seconds.
* Import the ``PiArm`` class from the ``piarm`` module, which is used to control PiArm.


.. code-block::

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])

Initialize the MCU first, then initialize the individual servo connection pins of PiArm and the connection pin of the bucket.

* ``PiArm( )``: Initialize the 3 servo pins on the Arm.
* ``bucket_init( )``: Set the pin of the bucket.
* ``set_offset( )``: Set the offset value of the 3 servos on the Arm.

.. code-block::

    while True:
        arm.set_bucket(-50)
        sleep(1)		
        arm.set_bucket(90)
        sleep(1)

This code is used to move the bucket back and forth between -50 and 90 degrees with a time interval of 1 second.

* ``set_bucket()``: Used to control the rotation angle of the bucket.

.. _py_clip:

Hanging Clip
--------------------

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 clip.py

After running the code, you will see the Hanging Clip repeatedly opening and closing. But you need to assemble :ref:`clip` first.


**Code**

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
    arm.hanging_clip_init(PWM('P3'))
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:
            arm.set_hanging_clip(-50)  		
            sleep(1)		
            arm.set_hanging_clip(90)		
            sleep(1)

* ``hanging_clip_init( )``: Used to initialize the pin of the Hanging Clip.
* ``set_hanging_clip( )``: used to set the rotation angle of the Hanging Clip. 

.. _py_electro:

Electromagnet
-------------------------

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 electromagnet.py

After running the code, you will see that **Electromagnet** is energized every second, the LED (D2) on the electromagnet lights up to indicate that it is energized, at which point it can attach some material with the iron.

But you need to assemble :ref:`electro` first.

**Code**

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
    arm.electromagnet_init(PWM('P3'))
    arm.set_offset([0,0,0])

    if __name__ == "__main__":
        while True:		
            arm.set_electromagnet('on')
            sleep(1)			
            arm.set_electromagnet('off')
            sleep(1)


* ``electromagnet_init( )``: Used to initialize the connection of the Electromagnet.
* ``set_electromagnet( )``: Used to control the Electromagnet on/off.







