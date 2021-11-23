Sound Effects
================

There are some music and sound effects built in Robot HAT, so we can let piarm make some sounds. In addition, piarm also provides the tts module to support its voice broadcast function.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/piarm/examples
    sudo python3 sounds_effects.py

After running the code, you will find that the piarm will play background music, change the music after ten seconds and start the countdown.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``piarm\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import Music,TTS
    from time import sleep

    m = Music()
    t = TTS()

    def sound():
        song = '../../Sound/Emergency_Alarm.wav'
        m.music_set_volume(40)
        print('Music duration',m.sound_length(song))
        m.sound_play(song)

    def background_music():
        music = '../../Music/peace.mp3'	
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

.. code-block::

    from robot_hat import Music,TTS

    m = Music()
    t = TTS()

Import the ``Music`` and ``TTS`` modules in the ``robot_hat`` package, and create an object ``m`` of the ``Music`` class and an object ``t`` of the ``TTS`` class to use the functions of music and voice broadcast.

The ``Music`` and ``TTS`` modules provide us with some functions to manipulate music files and voice output, such as:

``m.music_set_volume(40)`` is used to adjust the volume.

``m.sound_play(song)`` is used to play .wav audio files， ``m.background_music(music)`` is used to play .mp3 audio files,
the parameters are the path of the audio file.

``t.say("timing begins")`` the functions in the tts module are used for voice output character strings.

