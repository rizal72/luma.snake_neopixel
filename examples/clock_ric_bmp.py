#!/usr/bin/env python
import time
import locale
from pathlib import Path
from datetime import datetime

from luma.led_matrix.device import neopixel
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, ATARI_FONT
from PIL import ImageFont

from getCustomMapping import getMapping

locale.setlocale(locale.LC_ALL, '')

def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('luma.examples/examples/fonts', name))
    return ImageFont.truetype(font_path, size)

def minute_change(device):
    '''When we reach a minute change, animate it.'''
    hours = datetime.now().strftime('%H')
    minutes = datetime.now().strftime('%M')

    def helper(current_y):
        with canvas(device) as draw:
            draw.text((0,1), hours, font=fntbmp, fill=color1)
            draw.text((7,1),  ":", font=fntbmp, fill=color2)
            draw.text((8,current_y), minutes, font=fntbmp, fill=color1)
        time.sleep(0.1)
    for current_y in range(1, -8, -1):
        helper(current_y)
    minutes = datetime.now().strftime('%M')
    for current_y in range(-8, 1):
        helper(current_y)


def animation(device, from_y, to_y):
    '''Animate the whole thing, moving it into/out of the abyss.'''
    hourstime = datetime.now().strftime('%H')
    mintime = datetime.now().strftime('%M')
    current_y = from_y
    while current_y != to_y:
        with canvas(device) as draw:
            draw.text((0,current_y), hourstime, font=fntbmp, fill=color1)
            draw.text((7,current_y),  ":", font=fntbmp, fill=color2)
            draw.text((8,current_y), mintime, font=fntbmp, fill=color1)
        time.sleep(0.1)
        current_y += 1 if to_y > from_y else -1


def main():
    
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    # serial = spi(port=0, device=0, gpio=noop())
    # device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)

    device = neopixel(width=16, height=16, mapping=getMapping())
    device.contrast(16)
    
    global fntbmp
    global fnt
    global color1
    global color2

    color1 = "white"
    color2 = "yellow"
    fnt = proportional(ATARI_FONT)
    fntbmp = make_font("Volter__28Goldfish_29.ttf", int(device.height / 2))
   
    # The time ascends from the abyss...
    animation(device, -8, 1)
    
    toggle = False  # Toggle the second indicator every second
    while True:
        toggle = not toggle
        sec = datetime.now().second
        if sec == 59:
            # When we change minutes, animate the minute change
            minute_change(device)
        elif sec == 30:
                    # Half-way through each minute, display the complete date/time,
                    # animating the time display into and out of the abyss.
                    full_msg = time.ctime()
                    date_msg = time.strftime("%A, %d %b %Y")
                    animation(device, 1, -8)
                    show_message(device, date_msg, 8, fill=color2, font=fnt,scroll_delay=0.06)
                    animation(device, -8, 1)
        else:
            # Do the following twice a second (so the seconds' indicator blips).
            # I'd optimize if I had to - but what's the point?
            # Even my Raspberry PI2 can do this at 4% of a single one of the 4 cores!
            hours = datetime.now().strftime('%H')
            minutes = datetime.now().strftime('%M')
            with canvas(device) as draw:
                draw.text((0,1), hours, font=fntbmp, fill=color1)
                draw.text((7,1),  ":" if toggle else " ", font=fntbmp, fill=color2)
                draw.text((8,1), minutes, font=fntbmp, fill=color1)
    
            time.sleep(0.5)


if __name__ == "__main__":
    main()
