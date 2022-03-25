记忆功能
===================

PiArm提供了一个记录动作的功能，可以让PiArm自动做一些重复性的动作。

在这个项目中，我们来看下如何实现这个功能。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 memory_function.py

代码运行之后，你可以用左右摇杆来控制PiArm的转动和铲斗（但你需要先将 :ref:`shovel` 安装到PiArm上）, 按下左摇杆来记录PiArm的一次移动，记录了几组动作之后，你可以按下右摇杆来让PiArm来复现这些动作。

只记录点与点之间的变化，如果起点和终点是一样的，中间做了很多次移动，但只按下一次来记录，它会直接从起点到终点，不会记录中间过程。

**代码**


.. raw:: html

    <run></run>

.. code-block:: python 

    from robot_hat import Servo,PWM,Joystick,ADC,Pin
    from robot_hat.utils import reset_mcu
    from robot_hat import TTS
    from time import sleep
    from piarm import PiArm

    t = TTS()
    reset_mcu()
    sleep(0.01)

    leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
    rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

    arm = PiArm([1,2,3])
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])

    def _angles_control():
        arm.speed = 100
        flag = False
        alpha,beta,gamma = arm.servo_positions
        bucket = arm.component_staus
        global i	

        if leftJoystick.read_status() == "up":
            alpha += 1
            flag = True
        elif leftJoystick.read_status() == "down":
            alpha -= 1
            flag = True
        if leftJoystick.read_status() == "left":
            gamma += 1
            flag = True
        elif leftJoystick.read_status() == "right":
            gamma -= 1
            flag = True
        if rightJoystick.read_status() == "up":
            beta += 1
            flag = True
        elif rightJoystick.read_status() == "down":
            beta -= 1
            flag = True
            
        if rightJoystick.read_status() == "left": 	
            bucket += 2
            flag = True
        elif rightJoystick.read_status() == "right":
            bucket -= 2
            flag = True
            
        if leftJoystick.read_status() == "pressed":  	
            arm.record()
            t.say("record")
            print('step %s : %s'%(i,arm.steps_buff[i*2]))
            i += 1
            sleep(0.05)
        elif rightJoystick.read_status() == "pressed":

            t.say("action")
            arm.set_speed(80) 
            arm.record_reproduce(0.05)
            arm.set_speed(100)
            
        if flag == True:
            arm.set_angle([alpha,beta,gamma])
            arm.set_bucket(bucket)
            print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

    if __name__ == "__main__":
        print(arm.servo_positions)
        i = 0	
        while True:	
            _angles_control()
            sleep(0.01)

**它是如何工作的？**


在这个代码中，我们来重点看下 ``_angles_control()`` 函数，它是用来读取双摇杆的值之后，进行不同的操作。

1. 控制手臂的移动

.. code-block:: python

    if leftJoystick.read_status() == "up":
        alpha += 1
        flag = True
    elif leftJoystick.read_status() == "down":
        alpha -= 1
        flag = True
    if leftJoystick.read_status() == "left":
        gamma += 1
        flag = True
    elif leftJoystick.read_status() == "right":
        gamma -= 1
        flag = True
    if rightJoystick.read_status() == "up":
        beta += 1
        flag = True
    elif rightJoystick.read_status() == "down":
        beta -= 1
        flag = True

* ``alpha``, ``beta`` 和 ``gamma`` 分别指的是手臂上的3个舵机的角度，参考： :ref:`arm_angle`。
* 左摇杆向上拨动， ``alpha`` 增加，让手臂向前伸。
* 左摇杆向下拨动， ``alpha`` 减小，让手臂向里缩。
* 左摇杆向左拨动， ``gamma`` 增加，让手臂向左转动。
* 左摇杆向右拨动， ``gamma`` 减小，让手臂向右转动。
* 右摇杆向上拨动， ``beta`` 增加，让手臂向上。
* 右摇杆向下拨动， ``beta`` 减小，让手臂向下。

2. 控制铲斗的角度

.. code-block:: python

    if rightJoystick.read_status() == "left": 	
        bucket += 2
        flag = True
    elif rightJoystick.read_status() == "right":
        bucket -= 2
        flag = True

* 右摇杆向左拨动，让铲斗回卷
* 右摇杆向右拨动，让铲斗向外延伸。

3. 记录动作和复现动作

.. code-block:: python

    if leftJoystick.read_status() == "pressed":  	
        arm.record()
        t.say("record")
        print('step %s : %s'%(i,arm.steps_buff[i*2]))
        i += 1
        sleep(0.05)
    elif rightJoystick.read_status() == "pressed":

        t.say("action")
        arm.set_speed(80) 
        arm.record_reproduce(0.05)
        arm.set_speed(100)

* 如果左摇杆按下，调用 ``record()`` 函数来记录动作，PiArm会提示已记录。在终端会显示此时的角度及记录的动作数。
* 如果右摇杆按下，调用 ``record_reproduce()`` 函数来复现记录的动作，PiArm会提示开始做动作。

4. 将角度写给PiArm

.. code-block:: python

    if flag == True:
        arm.set_angle([alpha,beta,gamma])
        arm.set_bucket(bucket)
        print('servo angles: %s , bucket angle: %s '%(arm.servo_positions,arm.component_staus))

将手臂的角度和铲斗的角度写给PiArm，让它转动到这些角度。

如果你的臂端工具接的竖直夹或者是电磁铁，你可以参考以下链接来修改上面的代码：

* :ref:`py_clip_joystick`
* :ref:`py_electro_joystick`