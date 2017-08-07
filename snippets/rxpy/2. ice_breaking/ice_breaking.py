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
    # FILE: ice_breaking.py
=======================================================================================
"""

from rx import Observable, Observer
import lib.pycon.display as display


class PrintObserver(Observer):
    # `on_next` is general usage method, It will notice new data is received.
    def on_next(self, value):
        print('on_next value:%s' % (value))

    # `on_complete` will be fired when the observable is finally completed.
    def on_completed(self):
        print('on_completed !')

    # `on_error` is similar catch feature, You can detect an error and handle it.
    def on_error(self, value):
        print('on_error value:%s' % (value))


def observer_generator(observer):
    # Give "break" string to the observer we just created; I will run after subscribe method is called.
    observer.on_next("break")
    # And after, Give "the ice!" data, Yes it is similar .append or .push!
    observer.on_next("the ice!")

    # Recycle loop.
    while True:

        # Get some message, and use it.
        message = input()
        if message:
            # Pass the message we just got.
            observer.on_next(message)
        else:
            # If the message is empty, This code will be run.
            observer.on_completed()
            break


def main():
    # Create observable object for generate observer that can pass the data.
    observable = Observable.create(observer_generator)
    # Subscribe observable we just created, You can use a class for subscribing something.
    observable.subscribe(PrintObserver())

if __name__ == '__main__':
    # Display some awesome ASCII art.
    display.comment()
    # Start main business.
    main()
