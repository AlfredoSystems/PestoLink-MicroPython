# PestoLink-MicroPython
*v1.0.0*

PestoLink-MicroPython is a MicroPython module that runs on an XRP robot. By using the web app [PestoLink-Online](https://pestol.ink) you can connect to your robot with BLE (Bluetooth Low Energy) and drive the robot wirelessly.

You can drive using mobile or desktop. On desktop, you can drive with your keyboard or a gamepad (like an xbox controller or PS4 controller).

## XRP Robot Setup Guide ##
1) Connect to your robot with the [XRP code editor](https://xrpcode.wpi.edu/). CONNECT OVER USB. Do not connect over bluetooth, connecting over bluetooth can adversly effect PestoLink. If this is your first time connecting, prompts to update your XRP robot's MicroPython version and library version will appear. Make sure your Robot updates to the latest versions.

1) Upload `pestolink.py` to your XRP robot
	- [Click here](https://github.com/AlfredoSystems/PestoLink-MicroPython/archive/refs/heads/main.zip) to download this repository. After that, unzip it

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

1) Wireless use
	After you succesfully run `pestolink_example.py`, you can now disconnect the robot from the code editor. Even if you reset or power cycle the robot, it will automatically the most recently run file (`pestolink_example.py`) and you will still be able to connect to and drive your robot with PestoLink.

## Common issues ##
- Is your robot's battery dead or low?
- Is your USB cable "power only"?
- With the XRP code editor, you are connected over USB and not over Bluetooth?
- Do you have the latest firmware and library versions?
- Are you sure you are using a supported OS and browser?
- Is your Browser up to date?
- Make sure you have no duplicate tabs open, only one tab for the XRP code editor and one tab for PestoLink
- 
