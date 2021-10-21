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
for i in range(LED_NUM):
	#pixels[i] = (30, 0, 30)
	print(i)
	#if i > 5:
	pixels[i-10] = (0, 0, 0)

	pixels[i-9] = (5, 0, 5)
	
	pixels[i-8] = (10, 0, 10)
	
	pixels[i-7] = (15, 0, 15)
	
	pixels[i-6] = (20, 0, 20)
	
	pixels[i-5] = (40, 0, 40)
	
	pixels[i-4] = (60, 0, 60)
	
	pixels[i-3] = (80, 0, 80)

	pixels[i-2] = (100, 0, 100)

	pixels[i-1] = (150, 0, 150)
	
# Loop forever and blink the color
