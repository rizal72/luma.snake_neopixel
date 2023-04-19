#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Displays an animated gif.
"""

import sys
from pathlib import Path
from PIL import Image, ImageSequence
from luma.core.sprite_system import framerate_regulator
from lib.getCustomMapping import getMapping
from luma.led_matrix.device import neopixel

def main():
    regulator = framerate_regulator(fps=6)

    if len(sys.argv) > 1:
        gif = sys.argv[1]
    else:
        gif = 'ghost.gif'
        
    img_path = str(Path(__file__).resolve().parent.joinpath('', gif))
    image = Image.open(img_path)
    size = [min(*device.size)] * 2
    posn = ((device.width - size[0]) // 2, device.height - size[1])

    while True:
        for frame in ImageSequence.Iterator(image):
            with regulator:
                background = Image.new("RGB", device.size, "black")
                background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        device = neopixel(width=16, height=16, mapping=getMapping())
        device.contrast(10)
        main()
    except KeyboardInterrupt:
        pass
