游戏 - 收集铁片
==============================

在这个项目中，准备三角形，圆形，正方形3种形状的铁片，PiArm会随机说一种形状，你需要控制PiArm将相应形状的铁片放到相应的盒子里面。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 game_iron_collection.py

代码运行后，先按键盘上的 ``p`` 键来启动游戏，PiArm将提示游戏开始，然后随机说出一种形状（ ``Round``， ``Triangle`` 和 ``Square``），此时你可以用键盘上的 ``w``， ``s``， ``a``， ``d``， ``i``， ``k``， ``j`` 和 ``l`` 来控制PiArm来吸取对应形状的铁片。60秒后，将提示游戏结束，你将无法再控制PiArm。

如果你想停止代码运行，你需要先按下 ``Esc`` 键，然后再按 ``Ctrl+C``。

.. note::

    * 需要切换成小写来输入这些按键。
    * ``w``， ``s``， ``a``， ``d``， ``i`` 和 ``k`` 用来控制手臂的转动。
    * ``j`` 和 ``l`` 用来控制电磁铁的开关。

**代码**


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

**它是如何工作的？**

这个代码是在项目 :ref:`用键盘控制电磁铁` 的基础上加上了计时和说出随机形状的部分。

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

这个 ``timing()`` 函数是用来计时，提示游戏开始后，进行60秒的计时，然后进行3，2，1的倒计时报数，再提示游戏结束，让flag 为 False。

.. code-block:: python

    def say_shape():
        k = random.randint(1,3)
        if k == 1:
            t.say("Round")
        if k == 2:
            t.say("Triangle")
        if k == 3:
            t.say("Square")

这个 ``say_shape()`` 函数是让PiArm随机说出一种形状。


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

这是代码的主要流程：

* 在终端打印出按键提示，按下 ``p`` 来开始游戏，让 ``timing()`` 以单独的线程运行。
* 调用 ``readchar()`` 函数来读取键值。
* 如果读取到按键 ``p`` 被按下，就打印出按键提示，让 ``flag`` 为 ``True``，此时 ``timing()`` 函数开始计时, 3秒后，调用 ``say_shape()`` 函数来让PiArm随机说一个形状。
* 如果 ``flag`` 为 ``True``，调用 ``control()`` 函数来让PiArm根据按键值转动。
* ``chr(27)`` 为 ``Esc`` 按键， 如果 ``Esc`` 按键被按下，退出主循环。这一步是因为使用了 ``readchar()`` 函数一直读取键盘，所以无法直接通过 ``Ctrl+C`` 来停止代码运行。
* 此时就能通过 ``Ctrl+C`` 来停止代码运行。

