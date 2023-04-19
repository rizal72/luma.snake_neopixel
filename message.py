#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Displays an animated text.
"""

import sys
import time
import locale
from lib.getCustomMapping import getMapping
from luma.led_matrix.device import neopixel
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT, ATARI_FONT



def main():
    while True:
        show_message(device, text, y_offset=4, fill=color, font=proportional(ATARI_FONT), scroll_delay=0.05)
        time.sleep(1)


if __name__ == "__main__":

    locale.setlocale(locale.LC_ALL, '')
    
    try:
        device = neopixel(width=16, height=16, mapping=getMapping())
        text = "Questo e' un testo di prova..."
        color = "blue"

        if len(sys.argv) > 1:
            text = sys.argv[1]

        if len(sys.argv) > 2:
            color = sys.argv[2]
            
        main()
    except KeyboardInterrupt:
        pass
