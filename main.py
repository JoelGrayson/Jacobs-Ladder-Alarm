#!/usr/bin/env python3

# ABOUT: This is an executable

from time import sleep
from gpiozero import InputDevice, OutputDevice, LED
import requests
from ENVIRONMENT_VARIABLES import BRIDGE_IP, USERNAME

# Use the 
BUTTON_LED_OUT_GPIO=27
BUTTON_IN_GPIO=22
BUTTON_OUT_GPIO=23

button_led=LED(BUTTON_LED_OUT_GPIO)

# Pin 13 (GPIO 27) LED PWR
# Pin 14 LED GND (always GND)
# Pin 15 (GPIO 22) Btn in
# Pin 16 (GPIO 23) Btn out

"""
From `pinout`
GPIO27 (13) (14) GND
GPIO22 (15) (16) GPIO23
"""

def jacobs_ladder(state=False):
    print(f'Turning {"on" if state else "off"} Jacobs Ladder...')
    url=f'http://{BRIDGE_IP}/api/{USERNAME}/lights/3/state'
    print("Sending message to", url)
    requests.put(url, json={"on": state})

def listen_to_button():
    print('Listening to button...')
    btn_out=OutputDevice(BUTTON_OUT_GPIO) #for btn to receive input
    btn_out.on()
    btn_in=InputDevice(BUTTON_IN_GPIO) #read if button pressed
    #btn_in.when_pressed=lambda x:jacobs_ladder(False)
    while True: #Listen for button press
        if btn_in.is_active: #button pressed bc btn_in–btn_out circuit connected
            jacobs_ladder(False)


if __name__=='__main__':
    button_led.on()
    listen_to_button()

