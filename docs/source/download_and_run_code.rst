下载并运行代码
============================

首先通过在命令行中使用 ``git clone`` 下载库文件 ``robot-hat``。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://gitee.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    运行 ``setup.py`` 将下载一些必要的组件。 由于网络问题，你可能无法下载成功。你可能需要重新下载。
    在这种情况下，输入 Y 并按 Enter。
	
	.. image:: media/dowload_code.png

然后下载代码并安装 ``piarm`` 库。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b 2.0.0 https://gitee.com/sunfounder/piarm.git
    cd piarm
    sudo python3 setup.py install


这一步需要一点时间，所以请耐心等待。

最后需要运行脚本 ``i2samp.sh`` 安装i2s功放所需的组件，否则它可能会没有声音。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm
    sudo bash i2samp.sh
	
.. image:: media/i2s.png

输入 y 并按 Enter 继续运行脚本。

.. image:: media/i2s2.png

输入 y 并按 Enter 让 ``/dev/zero`` 在后台运行。

.. image:: media/i2s3.png

输入 y 并按 Enter 重新启动机器。

.. note::

    如果重新启动后没有声音，你可能需要多次运行i2samp.sh脚本。

运行 ``servo_zeroing.py``
--------------------------

因为舵机是靠Robot HAT上的电源供电的，当你只给树莓派供电时，舵机是不会工作的。你需要确保电池已放置在电池盒中且 Robot HAT 已通电。

.. image:: media/slide_to_power.png
    :width: 400
    :align: center


现在，运行 ``examples/`` 文件夹中的 ``servo_zeroing.py`` .

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 servo_zeroing.py

.. note:: 

    如果出现以下错误：

    self._smbus = SMBus(self._bus)
    FileNotFoundError: [Errno 2] No such file or directory
    
    请参考 :ref:`I2C 配置` 来启用树莓派的的 I2C 端口。

为确保你可以看到舵机已设置为0°，你可以先在舵机轴中插入摇臂，然后将舵机偏转一个任意角度。

.. image:: media/servo_arm.png
    :align: center

现在按照下图将舵机插入 P11 位置。

.. image:: media/pin11_connect.png
    :width: 400
    :align: center

如果伺服臂偏转并固定在一个角度，则说明该功能生效。如果不是，请检查伺服电缆的插入方向或重新运行代码。

.. note::

    在组装每个舵机之前，你需要将舵机引脚插入 P11 并保持通电。