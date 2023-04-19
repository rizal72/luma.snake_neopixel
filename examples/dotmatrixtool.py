#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Design a bitmap using http://dotmatrixtool.com/#, then paste the generated
hex values over those at lines 21-22.

See https://github.com/rm-hull/luma.led_matrix/issues/170
"""

import time
# from demo_opts import get_device
from luma.core.render import canvas
from luma.core import legacy
from getCustomMapping import getMapping
from luma.led_matrix.device import neopixel


def main():
    MY_CUSTOM_BITMAP_FONT = [
        [ 
        0x00, 0x30, 0x24, 0x40, 0x20, 0x24, 0x30, 0x00 
        ]
    ]

    # device = get_device()
    device = neopixel(width=16, height=16, mapping=getMapping())
    with canvas(device) as draw:
        # Note that "\0" is the zero-th character in the font (i.e the only one)
        legacy.text(draw, (0, 0), "\0", fill="white", font=MY_CUSTOM_BITMAP_FONT)

    time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
