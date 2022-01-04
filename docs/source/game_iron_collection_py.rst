GAME - Iron Collection
==============================

In this project, prepare 3 shapes of iron pieces: triangle, circle and square. PiArm will randomly say a shape, and you need to control PiArm to put the corresponding shape of iron pieces into the corresponding box.

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 game_iron_collection.py

After the code is run, first press ``p`` on the keyboard to start the game, PiArm will prompt the game to start, then randomly say a shape (``Round``, ``Triangle`` and ``Square``).
You need to use ``w``, ``s``, ``a``, ``d``, ``i`` and ``k`` on the keyboard to control Arm, ``j`` and ``l`` to pick up the corresponding shape (you need to install :ref:`Electromagnet` to PiArm first.).

60 seconds later, the game will be prompted to end and you will no longer be able to control the PiArm. If you want to stop the code from running, you need to press the ``Esc`` key first, then press ``Ctrl+C``.


.. note::

    * To switch the keyboard to lowercase English input.
    * ``w``, ``s``, ``a``, ``d``, ``i`` and ``k`` are used to control the rotation of the Arm.
    * ``j`` and ``l`` are used to control the ON and OFF of the Electromagnet.

**Code**


.. code-block:: python 

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS

    import threading
    import sys
    import tty
    import termios
    import random

    reset_mcu()
    sleep(0.01)
    t = TTS()

    arm = PiArm([1,2,3])
    arm.electromagnet_init(PWM('P3'))
    arm.set_offset([0,0,0])
    arm.speed = 100
    flag = False



    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    manual1 = '''
    Press keys on keyboard
        p: Game Start
        ESC: Stop
    '''

    manual2 = '''
    Press keys on keyboard
        w: extend
        s: retract    
        a: turn left
        d: turn right
        i: go up
        k: go down
        j: on
        l: off
    '''

    # def control():

    #     while flag == True:
    #         arm.speed = 100
    #         flag = False
    #         alpha,beta,gamma = arm.servo_positions

    def control(key):
        alpha,beta,gamma = arm.servo_positions	

        if key == 'a':
            gamma += 3		
        elif key == 'd':
            gamma -= 3		
        if key == 's':
            alpha -= 3
        elif key == 'w':
            alpha += 3		
        if key == 'i':
            beta += 3		
        elif key == 'k':
            beta -= 3		
        if key == 'j':
            arm.set_electromagnet('on')		
        elif key == 'l':
            arm.set_electromagnet('off')
        arm.set_angle([alpha,beta,gamma])
            

    def timing():
        global flag
        while True:
            if flag == True:
                t.say("game start") 
                sleep(60)
                t.say("three")  
                sleep(1)
                t.say("two")
                sleep(1)
                t.say("one")    
                sleep(1)
                t.say("game over")  
                flag = False

    def say_shape():
        k = random.randint(1,3)
        if k == 1:
            t.say("Round")
        if k == 2:
            t.say("Triangle")
        if k == 3:
            t.say("Square") 
        
    if __name__ == "__main__":

        print(manual1)

        thread1 = threading.Thread(target = timing) 
        thread1.start()     

        while True:
            key = readchar()
            if  key == 'p':
                print(manual2)
                flag = True
                sleep(3)
                say_shape()
            if flag == True:
                control(key)
            if key == chr(27):
                print("press ctrl+c to quit")
                break

**How it works?**

This code is based on the project :ref:`elec_keyboard` with the addition of timing and speaking random shapes.

.. code-block:: python

    def timing():
        global flag
        while True:
            if flag == True:
                t.say("game start") 
                sleep(60)
                t.say("three")  
                sleep(1)
                t.say("two")
                sleep(1)
                t.say("one")    
                sleep(1)
                t.say("game over")  
                flag = False

This ``timing()`` function is used for timing. After prompting the game to start, the game is timed for 60 seconds, then a countdown of 3, 2, 1 is performed before the game is prompted to end and the ``flag`` is set to ``False``.

.. code-block:: python

    def say_shape():
        k = random.randint(1,3)
        if k == 1:
            t.say("Round")
        if k == 2:
            t.say("Triangle")
        if k == 3:
            t.say("Square")

This ``say_shape()`` function is to make PiArm say a random shape.


.. code-block:: python

    if __name__ == "__main__":

        print(manual1)

        thread1 = threading.Thread(target = timing) 
        thread1.start()     

        while True:
            key = readchar()
            if  key == 'p':
                print(manual2)
                flag = True
                sleep(3)
                say_shape()
            if flag == True:
                control(key)
            if key == chr(27):
                break
        print("press ctrl+c to quit")

This is the main flow of the code.

* Print out the key prompt in the terminal and let ``timing()`` run in a separate thread.
* Call the ``readchar()`` function to read the key value.
* If key ``p`` is read as being pressed, print out the key prompt and let ``flag`` be ``True``, at which point the ``timing()`` function starts timing, and after 3 seconds, call the ``say_shape()`` function to make PiArm say a random shape.
* If ``flag`` is ``True``, call the ``control()`` function to make the PiArm rotate according to the key value.
* ``chr(27)`` represents the ``Esc`` key, and if the ``Esc`` key is pressed, exit the main loop. This step is because the ``readchar()`` function is used to read the keyboard all the time, so you can't stop the code directly with ``Ctrl+C``.
* At this point, you can stop the code with ``Ctrl+C``.
