#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Draw random dots
"""

import time
import random
from luma.led_matrix.device import neopixel
from luma.core.render import canvas
from lib.getCustomMapping import getMapping


def main():
    device = neopixel(width=16, height=16, mapping=getMapping())

    while True:
        with canvas(device) as draw:
            for i in range(4):
                x = random.randint(0, device.width)
                y = random.randint(0, device.height)

                # 'draw' is an ImageDraw object.
                draw.point((x, y), fill="white")
                time.sleep(0.05)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
