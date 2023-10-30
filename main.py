# Import necessary modules
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from XRPLib.defaults import *
import time
# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# 
axis1 = 127
axis2 = 127
axis3 = 127
axis4 = 127

# Define a callback function to handle received data
def on_rx(data):
    # Packet of bytes coming from PestoLink. teh fifth byte can also be used, each bit represents the state of one button
    byte_list = [byte for byte in data]
    
    axis1 = byte_list[1]
    axis2 = byte_list[2]
    axis3 = byte_list[3]
    axis4 = byte_list[4]


# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception
    
    #do stuff with the received data here
    print(axis1)
    
    power_L = (axis1 - 127) / 128
    power_R = (axis3 - 127) / 128
    
    drivetrain.set_effort(power_L, power_R)