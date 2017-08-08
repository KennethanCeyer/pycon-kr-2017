# -*- coding utf8 -*-

"""
=======================================================================================

    ██████╗ ██╗   ██╗ ██████╗ ██████╗ ███╗   ██╗    ██████╗  ██████╗  ██╗███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗████╗  ██║    ╚════██╗██╔═████╗███║╚════██║
    ██████╔╝ ╚████╔╝ ██║     ██║   ██║██╔██╗ ██║     █████╔╝██║██╔██║╚██║    ██╔╝
    ██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║╚██╗██║    ██╔═══╝ ████╔╝██║ ██║   ██╔╝
    ██║        ██║   ╚██████╗╚██████╔╝██║ ╚████║    ███████╗╚██████╔╝ ██║   ██║
    ╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═╝   ╚═╝


    ==                                PyCon 2017                                ==

    # AUTHOR: Kenneth (PIGNOSE)
    # DATE:   2017-08-13
    # FILE:   range.py
=======================================================================================
"""

import lib.pycon.display as display


# This is generator function!.
def custom_range(number):
    index = 0
    while(index < number):
        yield index
        index += 1


def main():
    # Original range function.
    for value in range(5):
        print(u'original range %d' % (value))

    # Add line escape.
    print(u'\n')

    # Custom range function.
    for value in custom_range(5):
        print(u'custom range %d' % (value))

if __name__ == '__main__':
    # Display some awesome ASCII art.
    display.comment()
    # Start main business.
    main()
