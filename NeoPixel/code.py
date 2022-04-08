import board
import digitalio
import time
import neopixel
from rainbowio import colorwheel
import random

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

num_pixels = 256

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 1

def rainbow():
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        return
    
def randompixels():
    alivetime = 300
    while alivetime:
        pixels[random.randrange(0, num_pixels)] = ((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        time.sleep(0.01)
        alivetime = alivetime - 1
        
def wipeout(color):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = (color)
        return
    
def drawPixels(sequence, position):
    
    for i in sequence:
        if i == 0:
            pixels[position] = ((0, 0, 0))
            position = position + 1
        if i == 1:
            pixels[position] = ((255, 0, 0))
            position = position + 1
        if i == 2:
            position = position + 6

#def displayChar(character, position):
#    match character:
#        case 'A':
#            print("Drawing A")
            

def scrollString(str_in, delay):
  import time
  str_in = str_in + " "
  strlen = len(str_in)
  offset = 0
  while True:
    for i in range(8):
      ch = str_in[(offset + 7 - i) % strlen]
      displayChar(ch, i)
    time.sleep(delay)
    offset = (offset + 1) % strlen
    
        
def split(word):
    return [char for char in word]
        
def drawText(characters):
    arr = split(characters)
    for i in arr:
        print(i)
    
#drawPixels([1, 0, 0, 0, 0, 1], 125)


while True:
    rainbow()
    wipeout((255, 0, 0))
    wipeout((0, 255, 0))
    wipeout((0, 0, 255))
    wipeout((0, 0, 0))
    randompixels()
    wipeout((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    pixels.fill((0, 0, 0))

