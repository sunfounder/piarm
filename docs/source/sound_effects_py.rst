音效
=====================

在本例中，我们使用 PiArm（准确地说是 Robot HAT）的音效。它由三部分组成，分别是Muisc、Sound、Text to Speech。

**安装 i2samp**

在使用该功能之前，请先激活扬声器，使其启用并可以发出声音。

运行 ``i2samp.sh``，此脚本将安装使用 i2s 放大器所需的一切。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/
    sudo bash i2samp.sh 

会有几个提示要求确认请求。用 ``Y`` 响应所有提示。对树莓派系统进行更改后，需要重新启动计算机才能使这些更改生效。

重新启动后， ``i2samp.sh`` 再次运行脚本以测试放大器。如果扬声器成功播放声音，则配置完成。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 sound_effect.py

代码运行后，PiArm会开始播放背景音乐，同时播放音效和说 \"timing begins\"，\"three\"，\"two\"，\"one\"，\"Stop music\"。

**代码** 

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Music,TTS
    from time import sleep

    m = Music()
    t = TTS()

    def sound():
        song = './sounds/sign.wav'
        m.music_set_volume(40)
        m.sound_play(song)

    def background_music():
        music = './musics/sports-Ahjay_Stelino.mp3'	
        m.music_set_volume(50)
        m.background_music(music)	

    def tts():
        t.say("timing begins")
        sleep(1)
        t.say("three")
        sleep(1)
        t.say("two")
        sleep(1)
        t.say("one")
        sleep(1)
        t.say("Stop music")
        sleep(1)
        
    if __name__ == "__main__":
        background_music()
        sleep(10)	
        #sound()
        #tts()
        while True:
            #background_music()
            sound()
            tts()		


**它是如何工作?**

这个代码很简单，创建了3个函数 ``sound()`` ， ``background()`` 和 ``tts()``, 然后分别调用它们来让PiArm播放音乐和说话。

.. code-block:: python

    def sound():
        song = './sounds/sign.wav'
        m.music_set_volume(40)
        m.sound_play(song)

以40%的音量播放音效 ``./sounds/sign.wav``。

* ``music_set_volume()``: 设置音量，范围是0%-100%。
* ``sound_play()``: 播放特定路径下音效。


.. code-block:: python

    def background_music():
        music = './musics/sports-Ahjay_Stelino.mp3'	
        m.music_set_volume(50)
        m.background_music(music)

以50%的音量播放背景音乐 ``./musics/sports-Ahjay_Stelino.mp3``。

* ``background_music()``：播放特定路径下的背景音乐。

.. code-block:: python

    def tts():
        t.say("timing begins")
        sleep(1)
        t.say("three")
        sleep(1)
        t.say("two")
        sleep(1)
        t.say("one")
        sleep(1)
        t.say("Stop music")
        sleep(1)

写文本到PiArm，让它说话。

* ``say()``：在括号中写入字符或字符串，就能让PiArm将它们说出来。