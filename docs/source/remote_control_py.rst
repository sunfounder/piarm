Remote Control
==================

In this project, we will use the keyboard keys WSADIKJL to control the piarm.

**Play Shovel Bucket**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control1.py

After running the code, you can use the keyboard to control the piarm and bucket, press the ESC key to exit.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)
    t = TTS()

    arm = PiArm([1,2,3])
    arm.bucket_init('P3')
    arm.set_offset([0,0,0])
    controllable = 0

    manual = '''
    Press keys on keyboard to record value!
        W: L_up
        A: L_left
        D: L_right
        S: L_down
        I: R_up
        J: R_left
        K: R_down
        L: R_right
        ESC: Quit
    '''

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def control(key):

        arm.speed = 100
        flag = False
        angle1,angle2,angle3 = arm.servo_positions	
        angle4 = arm.component_staus

        if key == 'a':
            angle3 += 3		
            flag = True
        elif key == 'd':
            angle3 -= 3		
            flag = True
        if key == 'j':
            angle4 += 2
            flag = True		
        elif key == 'l':
            angle4 += 2
            flag = True		
        if key == 's':
            angle1 -= 3
            flag = True
        elif key == 'w':
            angle1 += 3		
            flag = True
        if key == 'i':
            angle2 += 3		
            flag = True
        elif key == 'k':
            angle2 -= 3		
            flag = True
                            
        if flag == True:
            arm.set_angle([angle1,angle2,angle3])
            arm.set_bucket(angle4)		
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))
        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break	

**Play Hanging Clip**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control2.py

After running the code, you can use the keyboard to control the piarm and the hanging clip, press the ESC key to exit.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)
    t = TTS()

    arm = PiArm([1,2,3])
    arm.hanging_clip_init('P3')
    arm.set_offset([0,0,0])
    controllable = 0

    manual = '''
    Press keys on keyboard to record value!
        W: L_up
        A: L_left
        D: L_right
        S: L_down
        I: R_up
        J: R_left
        K: R_down
        L: R_right
        ESC: Quit
    '''

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def control(key):

        arm.speed = 100
        flag = False
        angle1,angle2,angle3 = arm.servo_positions	
        angle4 = arm.component_staus

        if key == 'a':
            angle3 += 3		
            flag = True
        elif key == 'd':
            angle3 -= 3		
            flag = True
        if key == 'j':
            angle4 += 2
            flag = True		
        elif key == 'l':
            angle4 += 2
            flag = True		
        if key == 's':
            angle1 -= 3
            flag = True
        elif key == 'w':
            angle1 += 3		
            flag = True
        if key == 'i':
            angle2 += 3		
            flag = True
        elif key == 'k':
            angle2 -= 3		
            flag = True
                            
        if flag == True:
            arm.set_angle([angle1,angle2,angle3])
            arm.set_hanging_clip(angle4)		
            print('servo angles: %s , clip angle: %s '%(arm.servo_positions,arm.component_staus))
        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break	

**Play Electromagnet**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control1.py

After running the code, you can use the keyboard to control the piarm and electromagnet, press the ESC key to exit.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)
    t = TTS()

    arm = PiArm([1,2,3])
    arm.electromagnet_init('P3')
    arm.set_offset([0,0,0])
    controllable = 0

    manual = '''
    Press keys on keyboard 
        W: L_up
        A: L_left
        D: L_right
        S: L_down
        I: R_up
        J: R_left
        K: R_down
        L: R_right
        ESC: Quit
    '''

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def control(key):

        arm.speed = 100
        flag = False
        angle1,angle2,angle3 = arm.servo_positions	
        status = ""

        if key == 'a':
            angle3 += 3		
            flag = True
        elif key == 'd':
            angle3 -= 3		
            flag = True
        if key == 'j':
            arm.set_electromagnet('on')
            status = "electromagnet is on"		
        elif key == 'l':
            arm.set_electromagnet('off')
            status = "electromagnet is off"		
        if key == 's':
            angle1 -= 3
            flag = True
        elif key == 'w':
            angle1 += 3		
            flag = True
        if key == 'i':
            angle2 += 3		
            flag = True
        elif key == 'k':
            angle2 -= 3		
            flag = True
                            
        if flag == True:
            arm.set_angle([angle1,angle2,angle3])	
            print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))
        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break	

**How it works?**

Similar to the previous project, but this time we control the rotation angle of the piarm servo by reading the value of the keyboard keys.

.. code-block::

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

Implement a function readchar(), read the key input, and return the pressed keyboard character. sys.stdin.read(1) can achieve this function,
But in order to avoid some special characters being escaped, we usually change the mode of the standard input stream before reading the key, and then change it back after reading.

* ``tty.setraw(sys.stdin.fileno)`` is to change the standard input stream to raw mode, that is, all characters will not be escaped during transmission, including special characters. Before changing the mode, back up the original mode, and restore it after the change.

* ``old_settings = termios.tcgetattr(fd)`` and ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` plays the role of backup and restore. ``fd`` is the `File descriptor <https://en.wikipedia.org/wiki/File_descriptor>`_ of the standard input stream.

.. code-block::

    while True:
        key = readchar()
        control(key)
        if key == chr(27):
            break

Then call ``readchar()`` to read the pressed key and assign it to the ``key``, and then call ``control(key)`` to control the movement of the piarm through the value of the ``key``.
``key == chr(27)`` means to press the esc key.	