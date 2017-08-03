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


class PrintObserver(Observer):

    def on_next(self, value):
        print('on_next value:{0}'.format(value))

    def on_completed(self):
        print('on_completed !')

    def on_error(self, value):
        print('on_error value:{0}'.format(value))


def observer_generator(observer):
    observer.on_next("hello")
    observer.on_next("world")

    while True:
        message = input()
        if message:
            observer.on_next(message)
        else:
            observer.on_completed()
            break


def main():
    observable = Observable.create(observer_generator)
    observable.subscribe(PrintObserver())

if __name__ == '__main__':
    display.comment()
    main()
