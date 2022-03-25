组装和测试3个臂端工具
===================================

这是第一个程序，也是你必须看到的程序。

在这个项目中，你将学习如何组装和使用 PiArm 的3个臂端工具。

.. _py_shovel:

铲斗
--------------------------

**运行代码**


.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 shovel.py

运行代码后，你将看到铲斗来回移动。但你需要先组装 :ref:`shovel`。

.. note::
    如果你发现舵机为0时，铲斗不是垂直向下的，需要松开舵机螺钉，再重新将铲斗以垂直向下的角度安装一遍。

**代码**


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

**它是怎么工作的**

.. code-block::

    from robot_hat import Robot,Servo,PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

* 首先，从 `robot_hat <https://robot-hat.readthedocs.io/en/latest/index.html>`_ 中导入 ``Robot``， ``servo``， ``PWM`` 等类。
* 从 ``robot_hat.utils`` 模块中导入 ``reset_mcu`` 类，用来复位MCU, 以免程序间的冲突，导致通信错误。
* 从 ``time`` 模块中导入 ``sleep`` 类，用来实现延时的功能，单位：秒。
* 从 ``piarm`` 模块中导入 ``PiArm`` 类别，这是用来控制PiArm。

.. code-block::

    reset_mcu()
    sleep(0.01)
    arm = PiArm([1,2,3])
    arm.bucket_init(PWM('P3'))
    arm.set_offset([0,0,0])

先初始化MCU，然后初始化PiArm的各个舵机连接引脚以及铲斗的连接引脚。

* ``PiArm()``：初始化手臂上的3个舵机引脚。
* ``bucket_init( )``：设置bucket的引脚。
* ``set_offset()``: 设置arm上的3个舵机的偏移值。

.. code-block::

    while True:
        arm.set_bucket(-50)
        sleep(1)		
        arm.set_bucket(90)
        sleep(1)

这段代码是用来让铲斗在-50和90度之间来回移动，时间间隔为1秒。

* ``set_bucket()``：用来控制铲斗的转动角度。

.. _py_clip:

竖直夹
--------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 clip.py

运行代码后，你将看到竖直夹重复的打开/闭合。但你需要先组装 :ref:`clip`。

.. note::
    如果你发现竖直夹在90°时，不是垂直向下并合拢。需要将竖直夹的固定螺钉取下，重新再安装一遍。


**代码**


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

* ``hanging_clip_init( )``：用来初始化竖直夹的引脚。
* ``set_hanging_clip()``：用来设置竖直夹的转动角度。 

.. _py_electro:

电磁铁
-------------------------

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 electromagnet.py

运行代码后，你会发现， **电磁铁** 每秒钟都会通电（电磁铁上的LED（D2）亮起，表明它通电了，这时可以用铁吸附一些材料。）。但你需要先组装 :ref:`electro`。

**代码**

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


* ``electromagnet_init( )``：用来初始化电磁铁的连接。
* ``set_electromagnet()``：用来控制电磁铁的开/关。







