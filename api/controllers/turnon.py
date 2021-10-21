# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example shows how to create a single pixel with a specific color channel
# order and blink it.
# Most NeoPixels = neopixel.GRB or neopixel.GRBW
# The 8mm Diffused NeoPixel (PID 1734) = neopixel.RGB
import time
import board
import neopixel
import sys
# Configure the setup
import board
import neopixel
LED_NUM=330
pixels = neopixel.NeoPixel(board.D18, LED_NUM)
# Create the NeoPixel object
#pixel = neopixel.NeoPixel(PIXEL_PIN, 1, pixel_order=ORDER)
red = int(sys.argv[1])
green = int(sys.argv[2])
blue = int(sys.argv[3])
colorCode = [red, green, blue]
colorCode.sort()
print(colorCode[-1])
counterUp = 100
counterDown = 50
pixels.brightness = 0
colorNum = 1
pixels.fill((red, green, blue))
# Loop forever and blink the color
for i in range(counterUp):
    lele = pixels.brightness
    brightness = 1/counterUp
    if i != 0:
        pixels.brightness += brightness
    time.sleep(0.00005)
    

