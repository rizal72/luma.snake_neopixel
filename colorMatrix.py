#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import randrange
#import numpy as np
from luma.led_matrix.device import neopixel
from luma.core.render import canvas
from lib.getCustomMapping import getMapping

def main():
    device = neopixel(width=16, height=16, mapping=getMapping())
    drawScreen(device)

def do_nothing(obj):
    pass

def drawScreen(device):
    device.cleanup = do_nothing
    for y in range(device.height):
        device.cleanup = do_nothing
        for x in range(device.width):
            device.cleanup = do_nothing
            with canvas(device) as draw:
                device.cleanup = do_nothing
                draw.point((x, y), fill=getRandomColor())
                time.sleep(1)

def getRandomColor():
    color = (randrange(255), randrange(255), randrange(255))
    return color

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass