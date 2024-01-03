#!/usr/bin/env python3

# ABOUT: This is an executable

from signal import pause
from gpiozero import LED, Button
from ENVIRONMENT_VARIABLES import BRIDGE_IP, USERNAME
import requests


# Pins
BUTTON_LED_OUT_GPIO=27
BUTTON_SIGNAL_GPIO=22

# Pin 13 (GPIO 27) LED PWR
# Pin 14 LED GND (always GND)
# Pin 15 (GPIO 22) Button signal
# Pin 3 Button GND (always GND)

# From `pinout`
# GPIO27 (13) (14) GND
# GPIO22 (15) (16) GPIO23


# Controls
button_led=LED(BUTTON_LED_OUT_GPIO)
button=Button(BUTTON_SIGNAL_GPIO)


def jacobs_ladder(state=False):
    print(f'Turning {"on" if state else "off"} Jacobs Ladder...')
    url=f'http://{BRIDGE_IP}/api/{USERNAME}/lights/3/state'
    print("Sending message to", url)
    requests.put(url, json={"on": state})


if __name__=='__main__':
    button_led.on()
    #listen_to_button()
    button.when_pressed=jacobs_ladder
    pause() #keep program running

