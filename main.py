import os
import array
import math
from time import sleep

width, height = os.get_terminal_size()
screen = array.array('u', ["0"] * (width * height))
# screen[width * height] = '\0'
aspect = width / height * (11.0 / 24.0)
for t in range(1000):
    for i in range(width):
        for j in range(height):
            x = i / width * 2.0 - 1.0
            y = j / height * 2.0 - 1.0
            x = x * aspect
            x = x + math.sin(t*0.01)
            pixel = ' '
            if (x*x+y*y) < 0.5: 
                pixel = "@"
            screen[i + j * width] = pixel
    print (*screen, sep='')