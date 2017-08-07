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
    # FILE: hello_world.py
=======================================================================================
"""

from rx import Observable, Observer
import lib.pycon.display as display


def observer_generator(observer):
    # Give "hello" string to the observer we just created; I will run after subscribe method is called.
    observer.on_next("hello")
    # And after, Give "world!" data, Yes it is similar .append or .push!
    observer.on_next("world!")

def main():
    # Create observable object for generate observer that can pass the data.
    observable = Observable.create(observer_generator)
    observable.subscribe(on_next=lambda value: print(value))

if __name__ == '__main__':
    # Display some awesome ASCII art.
    display.comment()
    # Start main business.
    main()
