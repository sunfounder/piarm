Sound Effects
=====================

In this example, we use the sound effects of PiArm (Robot HAT to be exact). It consists of three parts: Muisc, Sound, and Text to Speech.

**Install i2samp**

Before using this function, please activate the speaker so that it can produce sound.

Run ``i2samp.sh``, this script will install everything you need to use the i2s amplifier.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/
    sudo bash i2samp.sh 

There will be several prompts to confirm the request. Respond to all prompts with ``Y``. After making changes to the Raspberry Pi system, you will need to reboot the computer for these changes to take effect.

After restarting, ``i2samp.sh`` runs the script again to test the amplifier. If the speaker successfully plays sound, the configuration is complete.

**Run the code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 sound_effect.py

After the code is run, you will find that PiArm first plays the sound effect in the sound function, and then plays the background music. When the background music is played, the [tts] function is run for timing, and the countdown voice broadcast will be performed after 30 seconds.

**Code** 

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


**How it works?**

The code is simple, it creates 3 functions ``sound()``, ``background()`` and ``tts()``, and then calls them separately to make PiArm play music and speak.

.. code-block:: python

    def sound():
        song = './sounds/sign.wav'
        m.music_set_volume(40)
        m.sound_play(song)

Play the sound effect ``. /sounds/sign.wav`` at 40% volume.

* ``music_set_volume()``: Set volume, range is 0%-100%.
* ``sound_play()``: Play a sound in a specific path.


.. code-block:: python

    def background_music():
        music = './musics/sports-Ahjay_Stelino.mp3'	
        m.music_set_volume(50)
        m.background_music(music)

Play background music ``. /musics/sports-Ahjay_Stelino.mp3`` at 50% volume.

* ``background_music()``: Play the background music in a specific path.

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

Write text to PiArm to make it speak.

* ``say()``: Writing characters or strings in parentheses will make PiArm speak them out.