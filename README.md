# PestoLink-MircoPython
*v1.0.0*

PestoLink-MicroPython is a MicroPython script designed to run on an XRP robot. Then by using the web app [PestoLink-Online](https://pestol.ink) you can connect to your robot with BLE (Bluetooth Low Energy) and drive the robot wirelessly. You can drive using mobile or desktop. On desktop, you can drive with your keyboard or a gamepad (like an xbox controller or PS4 controller).


### XRP Robot Setup Guide ###
1) Your robot must use MicroPython version 1.21 or later
	- If your MicroPython version is less than that, then follow [these instructions to update it](https://micropython.org/download/RPI_PICO_W/)
1) If you updated to 1.21, then one of your XRP Kit's lib files will need a small tweak
	- Connect to your robot with the [XRP code editor](https://xrpcode.wpi.edu/)
	- Navigate to `lib > XRPLib > motor.py` and open the file `motor.py`
	- Add a new line on line 11 and paste in the following code: `self._speedPin.freq(50)`
	- It should look like this now:
```python
	def __init__(self, direction_pin: int, speed_pin: int, flip_dir:bool=False):
		self._dirPin = Pin(direction_pin, Pin.OUT)
		self._speedPin = PWM(Pin(speed_pin, Pin.OUT))
		self._speedPin.freq(50)
		self.flip_dir = flip_dir
		self._MAX_PWM = 65534 # Motor holds when actually at full power
```
	- Save the file to your robot with ctrl + s
1) Upload `pestolink.py` to your XRP robot
	- [Click here](https://github.com/AlfredoSystems/PestoLink-MicroPython/archive/refs/heads/main.zip) to download this repository. After that, unzip it
	- Connect to your robot with the [XRP code editor](https://xrpcode.wpi.edu/)
	- In the XRP Code editor, go to `file > Upload to XRP` and select `pestolink.py` from the repo you just downloaded
	- Save the file in the \lib folder, so that `FINAL PATH: /lib/pestolink.py`
1) Upload `pestolink_example.py` to your XRP robot
	- In the XRP Code editor, go to `file > Upload to XRP` and select `pestolink_example.py` from the repo you just downloaded
	- Save the file at the top level, so that `FINAL PATH: /pestolink_example.py`
1) Pairing and connecting
	- Open `pestolink_example.py`, change the `robot_name` string to whatever you would like the robot to show up as in the Bluetooth paring menu
	- Click the `Run` button in the top right
	- Go to [PestoLink-Online](https://pestol.ink). You will be faced with two options, for for now go with PestoLink-Mobile.
	- Press (or click if you are on desktop) `Connect BLE`. A pairing menu will appear. Find and select the robot name you chose. After the connection opens, you can now drive your robot!