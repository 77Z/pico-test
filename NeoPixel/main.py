import board
import neopixel
import time
from rainbowio import colorwheel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 256

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 1

def rainbow(speed):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(speed)

while True:
    rainbow(0)