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

pixels = neopixel.NeoPixel(board.GP0, num_pixels, auto_write=False)
pixels.brightness = 0.2

# This led board works off odds and evens due to the way it displays pixels
# Therefore, at the end of each row i made, I added 16 to the last number, and alternated between acending and decending rows

# This is a mapping for a 32x8 display
# The table of truth!

# truthtable = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,     128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, # Acending
#                 31,  30,  29,  28,  27,  26,  25,  24,  23,  22,  21,  20,  19,  18,  17,  16,     159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, # Decending
#                 32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,     160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, # Acending
#                 63,  62,  61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51,  50,  49,  48,     191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, # Decending
#                 64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,     192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, # Acending
#                 95,  94,  93,  92,  91,  90,  89,  88,  87,  86,  85,  84,  83,  82,  81,  80,     223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, # Decending
#                 96,  97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,     224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, # Acending
#                127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112,     255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240, # Decending
# ]

truthtable =   [   0,  31,  32,  63,  64,  95,  96, 127, 128, 159, 160, 191, 192, 223, 224, 255,       8,  23,  40,  55,  72,  87, 104, 119, 136, 151, 168, 183, 200, 215, 232, 247,
                   1,  30,  33,  62,  65,  94,  97, 126, 129, 158, 161, 190, 193, 222, 225, 254,       9,  22,  41,  54,  73,  86, 105, 118, 137, 150, 169, 182, 201, 214, 233, 246,
                   2,  29,  34,  61,  66,  93,  98, 125, 130, 157, 162, 189, 194, 221, 226, 253,      10,  21,  42,  53,  74,  85, 106, 117, 138, 149, 170, 181, 202, 213, 234, 245,
                   3,  28,  35,  60,  67,  92,  99, 124, 131, 156, 163, 188, 195, 220, 227, 252,      11,  20,  43,  52,  75,  84, 107, 116, 139, 148, 171, 180, 203, 212, 235, 244,
                   4,  27,  36,  59,  68,  91, 100, 123, 132, 155, 164, 187, 196, 219, 228, 251,      12,  19,  44,  51,  76,  83, 108, 115, 140, 147, 172, 179, 204, 211, 236, 243,
                   5,  26,  37,  58,  69,  90, 101, 122, 133, 154, 165, 186, 197, 218, 229, 250,      13,  18,  45,  50,  77,  82, 109, 114, 141, 146, 173, 178, 205, 210, 237, 242,
                   6,  25,  38,  57,  70,  89, 102, 121, 134, 153, 166, 185, 198, 217, 230, 249,      14,  17,  46,  49,  78,  81, 110, 113, 142, 145, 174, 177, 206, 209, 238, 241,
                   7,  24,  39,  56,  71,  88, 103, 120, 135, 152, 167, 184, 199, 216, 231, 248,      15,  16,  47,  48,  79,  80, 111, 112, 143, 144, 175, 176, 207, 208, 239, 240  ]

cmap = {
    "A":    [0,1,1,1,0,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,1,1,1,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9],
    "B":    [1,1,1,1,0,   9,
             1,0,0,0,1,   9,
             1,0,0,1,0,   9,
             1,1,1,1,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,1,1,1,0,   9],
    "C":    [0,1,1,1,1,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             0,1,1,1,1,   9],
    "D":    [1,1,1,0,0,   9,
             1,0,0,1,0,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,0,1,   9,
             1,0,0,1,0,   9,
             1,1,1,0,0,   9],
    "E":    [1,1,1,1,1,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,1,1,1,1,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,1,1,1,1,   9],
    "F":    [1,1,1,1,1,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,1,1,1,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9,
             1,0,0,0,0,   9],
    "redghost": [
             0,0,3,3,3,0,0, 9,
             0,3,3,3,3,3,0, 9,
             3,2,2,3,2,2,3, 9,
             3,4,2,3,4,2,3, 9,
             3,3,3,3,3,3,3, 9,
             3,3,3,3,3,3,3, 9,
             3,0,3,0,3,0,3, 9
    ]
}

def drawPixels(char, position):
    print("Drawing character " + char)
    for i in cmap[char]:
        if i == 0:
            pixels[truthtable[position]] = ((0, 0, 0))
            position = position + 1
        if i == 1:
            pixels[truthtable[position]] = ((255, 255, 255))
            position = position + 1
        if i == 2:
            pixels[truthtable[position]] = ((255, 0, 0))
            position = position + 1
        if i == 3:
            pixels[truthtable[position]] = ((0, 255, 0))
            position = position + 1
        if i == 4:
            pixels[truthtable[position]] = ((0, 0, 255))
            position = position + 1
        if i == 9:
            # position = position + 25
            position = position + 27
    pixels.show()

def scrollText(char, interval):
    for i in range(100):
        pixels.fill((0, 0, 0))
        drawPixels(char, i)
        time.sleep(interval)

def rainbow():
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[truthtable[i]] = colorwheel(pixel_index & 255)
            pixels.show()
        return
    
def randompixels():
    alivetime = 300
    while alivetime:
        pixels[random.randrange(0, num_pixels)] = ((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        time.sleep(0.01)
        alivetime = alivetime - 1
        pixels.show()
        
def wipeout(color):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = (color)
        return

def wipeoutoftruth(color):
    for j in range(255):
        for i in range(len(truthtable)):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[truthtable[i]] = (color)
            pixels.show()
            time.sleep(0.1)
        return



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


# charToBuffer("A", 2)

# drawPixels("A", 1)

# scrollText("A", 0.05)

rainbow()

# wipeoutoftruth((255, 0, 0))

# while True:

    # pixels[truthtable[22]] = ((255, 0, 0))
    # wipeoutoftruth((255, 0, 0))

    # pixels.fill((255, 255, 255))
    # time.sleep(0.001)
    # pixels.fill((0, 0, 0))
    # time.sleep(0.001)

    # pixels.fill((255, 255, 255))
    # time.sleep(0.05)
    # pixels.fill((0, 0, 0))
    # time.sleep(0.05)
    # wipeout((255, 255, 255))
    # rainbow()
    # wipeout((255, 0, 0))
    # wipeout((0, 255, 0))
    # wipeout((0, 0, 255))
    # wipeout((0, 0, 0))
# randompixels()
    # wipeout((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    # pixels.fill((0, 0, 0))

