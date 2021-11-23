Download and Run the Code
============================

Download the Piarm files by using ``git clone`` in the command line.


First change the directory to **/home/pi/** via `cd command <https://en.wikipedia.org/wiki/Cd_(command)>`_ .

.. raw:: html

    <run></run>

.. code-block:: 

    cd /home/pi/

Then clone the repository from github via `git clone command <https://github.com/git-guides/git-clone>`_ .

.. raw:: html

    <run></run>

.. code-block:: 

    git clone -b 2.0.0 https://github.com/sunfounder/piarm.git

.. _run_install.py:

Run install.py
-----------------------------------

Enter the following two commands to run the ``setup.py`` file in the ``piarm`` folder.

.. raw:: html

    <run></run>

.. code-block:: 

    cd piarm

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 setup.py install

The ``setup.py`` file will finish the installation of the required Python libraries, and configure the Raspberry Pi for Piarm operations.

.. image:: media/setup.png

.. warning::
    
    The ``setup.py`` program may encounter some **Errors** due to network connectivity. If there is an error prompt, please check the network and re-run ``setup.py`` until all processes show **Done** and the prompt **Finished** appears at the end.

This step can take several minutes. After the file is fully executed and the prompt **Finished** appears, please restart the Raspberry Pi.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo reboot