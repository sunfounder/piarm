坐标控制
======================

PiArm的手臂有2种控制模式： **角度控制** 和 **坐标控制**。

* **角度控制** 模式： 将一定的角度写入手臂的3个舵机，使手臂达到一个特定的位置。
* **坐标控制** 模式： 为手臂建立一个空间坐标系，并设置一个控制点，向这个控制点写入三维坐标，使手臂达到一个特定的位置。

本项目中使用了 **坐标控制** 模式。

关于手臂坐标的提示
--------------------------------

PiArm有一个空间矩形坐标系，其原点位于两侧舵机输出轴的中心点。控制点位于手臂的顶部，刻度单位为毫米。在初始状态下，控制点的坐标为（0，80，80）。

.. image:: media/coordinate0.png

需要注意的是，PiArm的臂长是有限的，如果坐标值的设置超过了其机械运动的极限，PiArm将旋转到一个不可预测的Position。

换句话说，PiArm的总臂长是160毫米，这意味着沿Y轴移动的控制点的极限值应该在（0,0,0）到（0,160,0）之间。但是，由于结构本身的限制，活动范围应该比这个范围小得多。


* X坐标的推荐范围是-80 ~ 80。
* Y坐标的推荐范围是30 ~ 130。
* Z坐标的建议范围是0 ~ 80。

铲斗 - 坐标控制
--------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 coord_control.py

代码运行后，代码运行后，你就能用拨动左右摇杆来控制PiArm的手臂的转动，分别按下左右摇杆来控制铲斗的角度。

但你需要先将 :ref:`铲斗` 安装到PiArm上。

**代码**

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
    arm.bucket_init(PWM('P3'))


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

        if leftJoystick.read_status() == "pressed": 	
            buket_angle += 1
            flag = True
        elif rightJoystick.read_status() == "pressed":
            buket_angle -= 1
            flag = True


        if flag == True:
            arm.do_by_coord([x,y,z])
            arm.set_bucket(buket_angle)
            print('coord: %s , bucket angle: %s '%(arm.current_coord,arm.component_staus))

    if __name__ == "__main__":
        while True:
            _coord_control()
            sleep(0.01)


在这个代码中，创建了函数 ``_coord_control()`` 来通过读取双摇杆模块的值来改变手臂的X，Y和Z的值。


* ``x``, ``y`` 和 ``z`` 分别指的是手臂的坐标，参考： :ref:`关于手臂坐标的提示`。
* 左摇杆向上拨动， ``y`` 增加，让手臂向前伸。
* 左摇杆向下拨动， ``y`` 减小，让手臂向里缩。
* 左摇杆向左拨动， ``x`` 增加，让手臂向左转动。
* 左摇杆向右拨动， ``x`` 减小，让手臂向右转动。
* 右摇杆向上拨动， ``z`` 增加，让手臂向上。
* 右摇杆向下拨动， ``z`` 减小，让手臂向下
* 最后，分别用左右摇杆的按键来控制铲斗的角度。


如果你的臂端工具接的竖直夹或者是电磁铁，你可以参考以下链接来修改上面的代码：

* :ref:`用摇杆控制竖直夹`
* :ref:`用摇杆控制电磁铁`