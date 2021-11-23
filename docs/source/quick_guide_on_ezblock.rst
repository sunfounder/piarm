Quick Guide on Ezblock
===========================

There are 2 parts here:

* :ref:`Before Assembling PiArm` allows you to keep all the servos at 0 degrees to complete a proper and safe assembly (otherwise you will probably damage the servos).
* :ref:`Before Programming With Ezblock` will guide you to download Ezblock Studio to play with PiArm.

Before Assembling PiArm
-----------------------------

Before assembling the PiArm, follow the instructions on how to install the Ezblock OS on an Micro SD card here: `Download and Install Ezblock OS <https://docs.sunfounder.com/projects/ezblock3/en/latest/quick_user_guide_for_ezblock3.html#download-and-install-ezblock-os>`_.

After burning the Ezblock system on the SD-card, the P11 port on the Robot HAT is set to calibrate the servo angle to 0°. To make sure the servo has been correctly set to 0°, first gently insert a rocker arm in the servo shaft, then slightly rotate the rocker arm to a different angle.

.. image:: media/servo_arm.png

Next, insert the servo cable into the P11 port as shown below:

.. image:: media/pin11_connect.png
    :width: 600

Turn on the **Power Switch** to the Robot HAT, and the servo arm should return to the 0° position. If the servo arm does not return to 0°, press the **RST** button to restart the Robot HAT.

.. note::

    Before mounting each servo, plug the servo cable into P11 and turn the power on to set the servo to 0°.

    This function will become invalid after writing any programs to the Micro SD card.



Before Programming With Ezblock
-------------------------------------
About EzBlock Studio installation and quick use tutorial，please refer to: `Install Ezblock Studio <https://docs.sunfounder.com/projects/ezblock3/en/latest/quick_user_guide_for_ezblock3.html#install-ezblock-studio>`_.

.. note::

    When you connect to PiArm on EzBlock Studio, you will be prompted to calibrate PiArm. This is because of possible deviations in the installation process or limitations of the servos themselves, making some servo angles slightly tilted, so you can calibrate them.
    
    But if you think the assembly is perfect and no calibration is needed, you can also skip this step.

