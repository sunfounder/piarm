GAME Ball Collection
==============================

Similar to the previous game, in this project we plan to use the ezblock control, TTS module and electromagnet to make another game. The voice broadcasts a shape, we need to suck the iron piece of the corresponding shape into the box within the specified time.

To implement this game, we only need to replace the clip with an electromagnet on the basis of the previous game, change the remote sensing operation to ezblock remote control and add a function ``say_shape()`` to randomly broadcast the shape of the iron piece.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 game_ball_collection.py

After running the code, press the keyboard buttons j and l together to start the game. The piarm will randomly broadcast a shape. Use wsadikjl to control the piarm to absorb the corresponding iron piece. After 60s, the countdown will start and the game will end when the countdown is over.
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

    import threading
    import sys
    import tty
    import termios
    import random

    reset_mcu()
    sleep(0.01)
    t = TTS()

    arm = PiArm([1,2,3])
    arm.electromagnet_init('P3')
    arm.set_offset([0,0,0])
    controllable = 0

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    manual = '''
    Press keys on keyboard to record value!
        W: L_up
        A: L_left
        S: L_right
        D: L_down
        I: R_up
        J: R_left
        K: R_down
        L: R_right
        ESC: Quit
    '''

    def control():

        while controllable == 1:
            arm.speed = 100
            flag = False
            angle1,angle2,angle3 = arm.servo_positions
            status = ""
        
            if leftJoystick.read_status() == "up":
                angle1 += 1
                flag = True
            elif leftJoystick.read_status() == "down":
                angle1 -= 1
                flag = True
            if leftJoystick.read_status() == "pressed": 
                arm.set_electromagnet('on')
                status = "electromagnet is on" 	
            elif rightJoystick.read_status() == "pressed":
                arm.set_electromagnet('off')
                status = "electromagnet is off"	                        
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
                print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))


    def timing():
        sleep(60)
        t.say("three")	
        sleep(1)
        t.say("two")
        sleep(1)
        t.say("one")	
        sleep(1)
        t.say("game over")	
        global controllable
        controllable = 0

    def say_shape():
        k = random.randint(1,3)
        if k == 1:
            t.say("Round")
        if k == 2:
            t.say("Triangle")
        if k == 3:
            t.say("Square")	
        
    if __name__ == "__main__":

        print(manual)

        thread1 = threading.Thread(target = control)
        thread2 = threading.Thread(target = timing)	
        i = 1
        while i:
            if 	readchar() == 'j' and readchar() == 'l':
                i = 0
                t.say("timing begins")
                controllable = 1
                thread1.start() 			
                thread2.start()	


**How it works?**

Similar to the previous game, we only need to change the joystick control and clip to keyboard control and electromagnet on the basis of the previous game, and add a random broadcast shape function.

.. code-block::

    def say_shape():
        k = random.randint(1,3)
        if k == 1:
            t.say("Round")
        if k == 2:
            t.say("Triangle")
        if k == 3:
            t.say("Square")	

The ``say_shape()`` function is used to randomly broadcast three shapes, among which ``random.randint(1,3)`` represents a random value from the three integers from 1 to 3。