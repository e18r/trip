#! /usr/bin/python

from random import choice

def next(prev):
    if prev == 1:
        return choice([0, 1])
    if prev == 6:
        return choice([-1, 0])
    return choice([-1, 0, 1])

def trip(length, last=None):
    if last is None:
        trip = [(choice(range(1, 7)), choice(range(1, 7)))]
    else:
        trip = [last]
    for i in range(1, length):
        prev_x = trip[i-1][0]
        prev_y = trip[i-1][1]
        while True:
            x = next(prev_x)
            y = next(prev_y)
            if x != 0 or y != 0:
                break
        trip.append((prev_x + x, prev_y + y))
    return trip

print(trip(2, (2,2)))
