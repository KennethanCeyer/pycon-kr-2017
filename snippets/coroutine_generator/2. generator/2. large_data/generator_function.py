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
    # FILE: generator_function.py
=======================================================================================
"""

from rx import Observable, Observer
import lib.pycon.display as display

# Define a dictionary variable for aggregate value by key.
dict = {}


def readfile(path):
    print('LOG: open `%s` file.' % (path))

    # Open file.
    fp = open(path, 'rb')

    # Get whole data, It maybe occurs heavy memory problem (For instance OutOfMemory).
    rows = []
    count = 0

    while True:
        if len(rows) >= 100:
            yield rows
            rows = []

        line = fp.readline()
        if not line:
            if len(rows) >= 100:
                yield rows
            break

        rows.append(line)
        count += 1

    print('LOG: %d lines read.' % (count))


def process(rows):
    # Iterate rows.
    for line in rows:
        # Split a line by comma.
        words = line.decode().split(',')

        # 3rd word is a key.
        name = words[2]
        # 1st word is a value.
        value = words[0]

        # If dictionary hasn't that key, Initialize to 0 value.
        if not name in dict:
            dict[name] = 0

        # Add value.
        dict[name] += int(value)

    # Return aggregated result.
    return dict


def main():
    # Input file path.
    PATH = './large_data.txt'

    # Read file and get string each of rows.
    for rows in readfile(PATH):
        # Calculate each of rows and aggregate value by keys.
        result = process(rows)

    # Divide line for print a result.
    print('========')

    # Iterate result by key.
    for key in result:
        # Print category name and aggregated value.
        print('`%s`: `%d`' % (key, result[key]))

if __name__ == '__main__':
    # Display some awesome ASCII art.
    display.comment()
    # Start main business.
    main()
