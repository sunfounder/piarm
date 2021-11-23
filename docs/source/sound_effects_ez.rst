Sound Effects
================

There is a built-in speaker in Robot HAT that can be used to play some music and sound effects, as well as to implement TTS functions.

Tips on Blocks
-------------------

* This block is a separate thread and can play some built-in background music.

.. image:: media/sound1.png

* This block can play some built-in sound effects.

.. image:: media/sound2.png

* You can write some text in this block and let PiArm speak them.

.. image:: media/sound3.png


Tips on Creating Functions
----------------------------

You may want to simplify the program with **Functions**, especially when you perform the same operation multiple times. Putting these operations into a newly declared function can greatly facilitate your use.

Click on the **Functions** category and select the appropriate function block, the function you created will also appear here.

.. image:: media/emotional2.png
  :width: 600

The **Function** block without output is used here.

.. image:: media/function_name.png

How to build code blocks
--------------------------

**Step 1**

Create a function named [music], put it in the code block [set background music volume to 50] and
[play background music peace.mp3] to play the peace.mp3 file at 50% volume.

.. image:: media/sound5.png

**Step 2**

Create a function named [sound] and put it into the code block [play sound effects Emergency_Alarm.wav with volum 50%]
to play the Emergency_Alarm.wav file at 50% volume.

.. image:: media/sound6.png

**Step 3**

Create a function named [tts], put the code block [say "something"] and [delay] to let piarm speak.

.. image:: media/sound73.png

**Step 4**

Put the three functions [sound], [music], [tts] into the [Forever] block to execute in turn.

.. image:: media/sound74.png

Complete Code
--------------------

Running this complete sample code, you will find that piarm first plays the sound effect in the sound function, and then plays the background music in the music function. When the background music is played, the tts function is run for timing, and the countdown voice broadcast will be performed after 30 seconds.

.. image:: media/sound5.png

.. image:: media/sound6.png

.. image:: media/sound7v2.png



