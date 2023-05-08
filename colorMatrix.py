#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import numpy as np
from luma.led_matrix.device import neopixel
from luma.core.render import canvas
from lib.getCustomMapping import getMapping

def main():
    device = neopixel(width=16, height=16, mapping=getMapping())

    for i in range(device.height):
        for l in range(device.width):
            with canvas(device) as draw:
                draw.point((i, l), fill=getRandomColor())
                time.sleep(0.1)

def getRandomColor():
    color = tuple(np.random.random(size=3) * 256)
    return color

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass