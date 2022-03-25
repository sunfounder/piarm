坐标模式
======================

PiArm 的手臂有 2 种控制模式: **角度** 和 **坐标**。

* :ref:`arm_angle`: 向 PiArm 手臂上的3个舵机写入一定的角度，使其到达特定位置。
* :ref:`arm_coor`: 为 PiArm 建立空间坐标系并设置控制点，将空间坐标写入该控制点，使其达到特定位置。

本项目通过坐标模式，设定2个坐标点，让机械臂将左边的橡皮鸭夹到右边的碗里。但你需要先将 :ref:`clip` 装到PiArm上。

.. image:: img/coor_usage.jpg
    :width: 500
    :align: center



**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 coordinate_mode.py

代码运行后，你就能看到PiArm将左边的橡皮鸭夹到右边的碗里。

但你需要先将 :ref:`clip` 安装到PiArm上。


**代码**

.. raw:: html

    <run></run>

.. code-block:: python

    from re import M
    from robot_hat import PWM
    from robot_hat.utils import reset_mcu
    from time import sleep
    from piarm import PiArm

    reset_mcu()
    sleep(0.01)

    " Grab an object from one coordinate to another coordinate"

    arm = PiArm([1,2,3])
    arm.set_offset([0,0,0])
    arm.hanging_clip_init(PWM('P3'))


    if __name__ == "__main__":

        start_coord = [-100, 40, 20] # x,y,z
        end_coord = [100, 40, 30] # x,y,z
        

        arm.set_speed(60)
        arm.set_hanging_clip(20)
        arm.do_by_coord(start_coord)
        arm.set_hanging_clip(90)

        start_coord_up = [start_coord[0], start_coord[1], 80]
        arm.do_by_coord(start_coord_up)

        end_coord_up = [end_coord[0], end_coord[1], 80]
        arm.do_by_coord(end_coord_up)

        arm.do_by_coord(end_coord)
        arm.set_hanging_clip(20)
        arm.do_by_coord(end_coord_up)


**它是如何工作的？**


.. code-block:: python

    start_coord = [-100, 40, 20] # x,y,z
    end_coord = [100, 40, 30] # x,y,z

* ``start_coord``：左边橡皮鸭的坐标。
* ``end_coord``: 右边碗的坐标。

.. note::

    * 这里的坐标都是指的控制点的坐标，但是装好臂端工具后，X和Y坐标的实际距离大一点。
    * 不同的臂端工具，误差距离不一样。比如竖直夹和电磁铁为3-4cm, 铲斗为6-7cm。
    * 比如在这里X坐标写的是100，但实际距离是13-14cm。
    * 一般建议X的坐标是-80 ~ 80，但由于这里Y坐标值较小（建议范围是30~130），所以设置为100也是能到的。但如果你增大了Y坐标值，由于连杆作用，X坐标值需要根据实际情况调小一点。


.. code-block:: python

        arm.set_speed(60)
        arm.set_hanging_clip(20)
        arm.do_by_coord(start_coord)
        arm.set_hanging_clip(90)

        start_coord_up = [start_coord[0], start_coord[1], 80]
        arm.do_by_coord(start_coord_up)

        end_coord_up = [end_coord[0], end_coord[1], 80]
        arm.do_by_coord(end_coord_up)

        arm.do_by_coord(end_coord)
        arm.set_hanging_clip(20)
        arm.do_by_coord(end_coord_up)

* PiArm先张开竖直夹（20°），然后转动到左边橡皮鸭的位置（ ``start_coord`` ），再合拢竖直夹（90°）。
* PiArm抬起头（ ``start_coord_up`` ），再转动到右边的碗的正上方（ ``end_coord_up``）。
* PiArm低头（ ``end_coord``）， 再张开竖直夹（20°）让橡皮鸭掉落到碗里，最后再抬起头（ ``end_coord_up``）。