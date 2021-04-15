#!/usr/bin/env python3

import pyperclip
import keyboard

while True:
    if keyboard.is_pressed('p') and keyboard.is_pressed('ctrl'):
        keyboard.write(pyperclip.paste())