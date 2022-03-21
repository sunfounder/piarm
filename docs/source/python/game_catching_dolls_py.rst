游戏 - 抓娃娃
==============================

现在我们来玩一个抓娃娃的游戏，看看谁能在规定的时间内用PiArm抓到更多的娃娃。
为了玩这个游戏，我们需要实现两个功能，第一个功能是用双摇杆模块控制PiArm，第二个功能是计时，当倒计时结束后，我们就不能再控制PiArm。这两部分必须同时执行。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 game_catching_dolls.py

代码运行后，同时按下左右摇杆来开始游戏，此时你就可以用双摇杆模块来控制PiArm来抓取娃娃，请注意时间，60秒之后，PiArm将提示游戏结束，你将无法再继续操作PiArm。

**代码**

.. raw:: html

    <run></run>

.. code-block:: python 

    from robot_hat import Servo,PWM,Joystick,ADC,Pin
    from robot_hat.utils import reset_mcu
    from time import sleep
    from robot_hat import TTS
    import threading

    from piarm import PiArm

    reset_mcu()
    sleep(0.01)
    t = TTS()

    leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
    rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

    arm = PiArm([1,2,3])
    arm.hanging_clip_init(PWM('P3'))
    arm.set_offset([0,0,0])
    arm.speed = 100
    game_flag = 0

    def control():

        alpha,beta,gamma = arm.servo_positions
        clip = arm.component_staus

        if leftJoystick.read_status() == "up":
            alpha += 1
        elif leftJoystick.read_status() == "down":
            alpha -= 1
        if leftJoystick.read_status() == "left":
            gamma += 1
        elif leftJoystick.read_status() == "right":
            gamma -= 1
        if rightJoystick.read_status() == "up":
            beta += 1
        elif rightJoystick.read_status() == "down":
            beta -= 1
        if leftJoystick.read_status() == "pressed":  	
            clip += 1
        elif rightJoystick.read_status() == "pressed":	
            clip -= 1


        # if key_flag == True:
        arm.set_angle([alpha,beta,gamma])
        arm.set_hanging_clip(clip)
            # print('coord: %s , servo angles: %s , clip angle: %s '%(arm.current_coord,arm.servo_positions,arm.component_staus))

    def timing():
        sleep(60)
        t.say("three")
        sleep(1)
        t.say("two")
        sleep(1)
        t.say("one")	
        sleep(1)
        t.say("game over")	
        global game_flag
        game_flag = 0	

    if __name__ == "__main__":

        thread1 = threading.Thread(target = timing)	
        thread1.start()	
        print("Press two joysticks at the same time to start the game")
        
        while True:
            if 	leftJoystick.read_status() == "pressed" and rightJoystick.read_status() == "pressed":
                t.say("timing begins")
                game_flag = 1		
            if game_flag == 1:
                control()


**它是如何工作的?**


这个代码是在 :ref:`用摇杆控制竖直夹` 项目的基础上加上了计时。

.. code-block:: python

    def timing():
        sleep(60)
        t.say("three")
        sleep(1)
        t.say("two")
        sleep(1)
        t.say("one")	
        sleep(1)
        t.say("game over")	
        global game_flag
        game_flag = 0	

使用 ``sleep()`` 函数进行60秒的计时，随后就让PiArm进行3，2，1倒计时报数，时间到了之后，让 ``game_flag`` 为0，此时将无法再控制PiArm。

.. code-block:: python

    if __name__ == "__main__":

        thread1 = threading.Thread(target = timing)	
        thread1.start()	
        print("Press two joysticks at the same time to start the game")


让 ``timing()`` 函数以另外一个线程运行，这样就可以在控制PiArm的同时，进行计时。

.. code-block:: python

        while True:
            if 	leftJoystick.read_status() == "pressed" and rightJoystick.read_status() == "pressed":
                t.say("timing begins")
                game_flag = 1		
            if game_flag == 1:
                control()

这是代码的主要流程，当左右摇杆同时按下时，PiArm说计时开始，让 ``game_flag`` 为1，此时就可以调用 ``control()`` 函数来控制PiArm。




