# PestoLink-MicroPython
*v1.0.0*

PestoLink-MicroPython is a MicroPython script that runs on an XRP robot. By using the web app [PestoLink-Online](https://pestol.ink) you can connect to your robot with BLE (Bluetooth Low Energy) and drive the robot wirelessly.

You can drive using mobile or desktop. On desktop, you can drive with your keyboard or a gamepad (like an xbox controller or PS4 controller).

## XRP Robot Setup Guide ##
1) Your robot needs to use MicroPython version 1.21 or later
	- If your MicroPython version is less than that, then follow [these instructions to update it](https://micropython.org/download/RPI_PICO_W/)

1) Upload `pestolink.py` to your XRP robot
	- [Click here](https://github.com/AlfredoSystems/PestoLink-MicroPython/archive/refs/heads/main.zip) to download this repository. After that, unzip it
	- Connect to your robot with the [XRP code editor](https://xrpcode.wpi.edu/)
	- In the XRP Code editor, go to `file > Upload to XRP` and select `pestolink.py` from the repo you just downloaded
	- Save the file in the \lib folder, so that `FINAL PATH: /lib/pestolink.py`

1) Upload `pestolink_example.py` to your XRP robot
	- In the XRP Code editor, go to `file > Upload to XRP` and select `pestolink_example.py` from the repo you just downloaded
	- Save the file at the top level, so that `FINAL PATH: /pestolink_example.py`

1) Pairing and connecting
	- Open `pestolink_example.py`, change the `robot_name` string to what you want the robot to be named for Bluetooth pairing
	- Click the `Run` button in the top right
	- Go to [PestoLink-Online](https://pestol.ink). You will be faced with two options, go with PestoLink-Mobile for now but you can try the gamepad version later if you want
	- Press/click `Connect BLE`. A pairing menu will appear, find and select the robot name you chose. After the connection opens, you can now drive your robot!
