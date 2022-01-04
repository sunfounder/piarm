远程控制
==================

在这个项目中，我们将使用键盘上的 ``w``， ``s``， ``a``， ``d``， ``i``， ``k``， ``j`` 和 ``l`` 来控制PiArm。


用键盘控制铲斗
---------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control1.py

运行代码之后，按照提示，按下键盘上的按键来控制PiArm的手臂和铲斗。

但你需要先将 :ref:`铲斗` 安装到PiArm上。

.. note::

    * 需要切换成小写来输入这些按键。
    * ``w``， ``s``， ``a``， ``d``， ``i`` 和 ``k`` 用来控制手臂的转动。
    * ``j`` 和 ``l`` 用来控制铲斗的角度。

**代码**


.. code-block:: python

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)

    arm = PiArm([1,2,3])
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])
    controllable = 0


    manual = '''
    Press keys on keyboard
        w: extend
        s: retract    
        a: turn left
        d: turn right
        i: go up
        k: go down
        j: open
        l: close
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
        alpha,beta,gamma = arm.servo_positions	
        bucket = arm.component_staus

        if key == 'w':
            alpha += 3
            flag = True
        elif key == 's':
            alpha -= 3		
            flag = True
        if key == 'a':
            gamma += 3		
            flag = True
        elif key == 'd':
            gamma -= 3		
            flag = True	
        if key == 'i':
            beta += 3		
            flag = True
        elif key == 'k':
            beta -= 3		
            flag = True
        if key == 'j':
            bucket -= 1
            flag = True		
        elif key == 'l':
            bucket += 1
            flag = True	

        if flag == True:
            arm.set_angle([alpha,beta,gamma])
            arm.set_bucket(bucket)		
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break		


**它是如何工作的？**

.. code-block:: python

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

该功能引用标准输入流并返回读取的数据流的第一个字符。

* ``tty.setraw(sys.stdin.fileno)`` 就是将标准输入流改为raw模式，即传输过程中所有字符都不会被转义，包括特殊字符。
* ``old_settings = termios.tcgetattr(fd)`` 和 ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` 并起到备份和恢复的作用。

.. code-block:: python

    def control(key):

        arm.speed = 100
        flag = False
        alpha,beta,gamma = arm.servo_positions	
        bucket = arm.component_staus

        if key == 'w':
            alpha += 3
            flag = True
        elif key == 's':
            alpha -= 3		
            flag = True
        if key == 'a':
            gamma += 3		
            flag = True
        elif key == 'd':
            gamma -= 3		
            flag = True	
        if key == 'i':
            beta += 3		
            flag = True
        elif key == 'k':
            beta -= 3		
            flag = True
        if key == 'j':
            bucket -= 1
            flag = True		
        elif key == 'l':
            bucket += 1
            flag = True	

        if flag == True:
            arm.set_angle([alpha,beta,gamma])
            arm.set_bucket(bucket)		
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

在这个代码中，创建了 ``control()`` 函数来通过读取键盘上的键值来控制PiArm。

* ``alpha``, ``beta`` 和 ``gamma`` 分别指的是手臂上的3个舵机的角度，参考： :ref:`关于手臂的转动角度提示`。
* 按下键盘上的 ``w`` 键， ``alpha`` 增加，让手臂向前伸。
* 按下键盘上的 ``s`` 键， ``alpha`` 减小，让手臂向里缩。
* 按下键盘上的 ``a`` 键， ``gamma`` 增加，让手臂向左转动。
* 按下键盘上的 ``d`` 键， ``gamma`` 减小，让手臂向右转动。
* 按下键盘上的 ``i`` 键， ``beta`` 增加，让手臂向上。
* 按下键盘上的 ``k`` 键， ``beta`` 减小，让手臂向下。
* 最后，分别用 ``k`` 和 ``l`` 按键来控制铲斗的角度。

.. code-block:: python

    while True:
        key = readchar()
        control(key)
        if key == chr(27):
            break

在主程序中调用 ``readchar()`` 来读取按键值，然后将读取的键值传入到 ``control()`` 函数中，这样PiArm就会根据不同的按键来移动。
``key == chr(27)`` 代表按键 ``Esc`` 按键。

用键盘控制竖直夹
-------------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control2.py

运行代码之后，按照提示，按下键盘上的按键来控制PiArm的手臂和竖直夹。

但你需要先将 :ref:`竖直夹` 安装到PiArm上。

.. note::

    * 需要切换成小写来输入这些按键。
    * ``w``， ``s``， ``a``， ``d``， ``i`` 和 ``k`` 用来控制手臂的转动。
    * ``j`` 和 ``l`` 用来控制竖直夹的角度。

**代码**


.. code-block:: python

    from piarm import PiArm
    from robot_hat import Pin,PWM,Servo,ADC
    from time import time,sleep
    from robot_hat.utils import reset_mcu

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)

    arm = PiArm([1,2,3])
    arm.hanging_clip_init(PWM('P3'))
    arm.set_offset([0,0,0])
    controllable = 0


    manual = '''
    Press keys on keyboard
        w: extend
        s: retract    
        a: turn left
        d: turn right
        i: go up
        k: go down
        j: open
        l: close
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
        alpha,beta,gamma = arm.servo_positions	
        clip = arm.component_staus

        if key == 'w':
            alpha += 3
            flag = True
        elif key == 's':
            alpha -= 3		
            flag = True
        if key == 'a':
            gamma += 3		
            flag = True
        elif key == 'd':
            gamma -= 3		
            flag = True	
        if key == 'i':
            beta += 3		
            flag = True
        elif key == 'k':
            beta -= 3		
            flag = True
        
        if key == 'j':
            clip -= 1
            flag = True		
        elif key == 'l':
            clip += 1
            flag = True	
        
        if flag == True:
            arm.set_angle([alpha,beta,gamma])
            arm.set_hanging_clip(clip)		
            print('servo angles: %s , clip angle: %s '%(arm.servo_positions,arm.component_staus))

        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break	

在这个代码中，创建了 ``control()`` 函数来通过读取键盘上的键值来控制PiArm。

* ``alpha``, ``beta`` 和 ``gamma`` 分别指的是手臂上的3个舵机的角度，参考： :ref:`关于手臂的转动角度提示`。
* 按下键盘上的 ``w`` 键， ``alpha`` 增加，让手臂向前伸。
* 按下键盘上的 ``s`` 键， ``alpha`` 减小，让手臂向里缩。
* 按下键盘上的 ``a`` 键， ``gamma`` 增加，让手臂向左转动。
* 按下键盘上的 ``d`` 键， ``gamma`` 减小，让手臂向右转动。
* 按下键盘上的 ``i`` 键， ``beta`` 增加，让手臂向上。
* 按下键盘上的 ``k`` 键， ``beta`` 减小，让手臂向下。
* 最后，分别用 ``k`` 和 ``l`` 按键来控制竖直夹的角度。

用键盘控制电磁铁
--------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 keyboard_control1.py

运行代码之后，按照提示，按下键盘上的按键来控制PiArm的手臂和电磁铁。

但你需要先将 :ref:`电磁铁` 安装到PiArm上。

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

    import sys
    import tty
    import termios

    reset_mcu()
    sleep(0.01)

    arm = PiArm([1,2,3])
    arm.electromagnet_init(PWM('P3'))
    arm.set_offset([0,0,0])
    controllable = 0


    manual = '''
    Press keys on keyboard
        w: extend
        s: retract    
        a: turn left
        d: turn right
        i: go up
        k: go down
        j: on
        l: off
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
        alpha,beta,gamma = arm.servo_positions	
        status = ""

        if key == 'w':
            alpha += 3
            flag = True
        elif key == 's':
            alpha -= 3		
            flag = True
        if key == 'a':
            gamma += 3		
            flag = True
        elif key == 'd':
            gamma -= 3		
            flag = True	
        if key == 'i':
            beta += 3		
            flag = True
        elif key == 'k':
            beta -= 3		
            flag = True

        if key == 'j':
            arm.set_electromagnet('on')		
        elif key == 'l':
            arm.set_electromagnet('off')
            
        if flag == True:
            arm.set_angle([alpha,beta,gamma])	
            print('servo angles: %s , electromagnet status: %s '%(arm.servo_positions,status))

        
    if __name__ == "__main__":

        print(manual)

        while True:
            key = readchar()
            control(key)
            if key == chr(27):
                break		

在这个代码中，创建了 ``control()`` 函数来通过读取键盘上的键值来控制PiArm。

* ``alpha``, ``beta`` 和 ``gamma`` 分别指的是手臂上的3个舵机的角度，参考： :ref:`关于手臂的转动角度提示`。
* 按下键盘上的 ``w`` 键， ``alpha`` 增加，让手臂向前伸。
* 按下键盘上的 ``s`` 键， ``alpha`` 减小，让手臂向里缩。
* 按下键盘上的 ``a`` 键， ``gamma`` 增加，让手臂向左转动。
* 按下键盘上的 ``d`` 键， ``gamma`` 减小，让手臂向右转动。
* 按下键盘上的 ``i`` 键， ``beta`` 增加，让手臂向上。
* 按下键盘上的 ``k`` 键， ``beta`` 减小，让手臂向下。
* 最后，分别用 ``k`` 和 ``l`` 按键来控制电磁铁的开关。