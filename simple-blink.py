#!/usr/bin/python3
#   simple-blink.py                     3/23/2022
#   drives 3 LEDs on my breadboard "bbmini"

from gpiozero import LED
import os, subprocess, time, json
#from gpiozero import Servo, Button
#from signal import signal, SIGTERM, SIGHUP, pause
ledb = LED(13)
ledy = LED(19)
ledr = LED(26)
leds = [ledr,ledy,ledb]

def allOff():
    for i in range(len(leds)):
        leds[i].off(); 

for i in range(4): 
    ledr.on(); time.sleep(0.2); ledr.off(); time.sleep(0.2)
time.sleep(1)

for k in range(20):    
    i = k %3
    leds[i].on(); time.sleep(0.1); leds[i].off(); time.sleep(0.1);

allOff()

