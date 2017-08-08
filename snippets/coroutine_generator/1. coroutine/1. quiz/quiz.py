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
    # FILE:   quiz.py
=======================================================================================
"""

import random
import lib.pycon.display as display


# This is co-routine function!.
def quiz(number):
    while True:
        pick = (yield)
        if pick > number:
            print('Your number is bigger than my one.')
        elif pick < number:
            print('Your number is smaller than my one.')
        elif pick == number:
            print('Yes! exactly same my one.')
            yield True


def main():
    # Get one of random numbers from 1 to 100.
    initial = random.randrange(1, 100)

    # Give initial number to co-routine.
    co_routine = quiz(initial)
    next(co_routine)

    print('Enter any number, But zero means exit.')

    while True:

        # Get string value from user.
        pick = input()

        # Convert string to number safely.
        try:
            pick_number = int(pick)
        except ValueError:
            print('Please try valid number.')
            continue

        # If the value is zero, Break the loop and exit the program
        if pick_number == 0:
            print('Good bye~')
            break

        # Get result for checking what it is correct.
        result = co_routine.send(pick_number)

        # If user has correct value, Break loop.
        if result is True:
            print('Co-routine is done, Exit the program.')
            co_routine.close()
            break

if __name__ == '__main__':
    # Display some awesome ASCII art.
    display.comment()
    # Start main business.
    main()
