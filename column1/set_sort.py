#!/usr/bin/env python
import blist
"""
1. If memory were not scarce, how would you implement a sort in a
language with libraries for representing and sorting sets?

Why? The friendly conversation between Bentley and his friend discuss
the question.

Q: Is there anything else that you can tell me about the records?

A: The recrods are phone numbers. In the US a phone number is a
seven-digit positive integer with no other associated data.

examples:
    (765) 2,372,240
    (917) 6,028,415
    (917) 9,999,999

The largest telephone number is 9,999,999 which is less than 10**7.
"""

def int_sort(infile, outfile):
    a = []
    with open(infile, 'rb') as fp:
        for line in fp:
            a.append(int(line.rstrip('\n')))

    a.sort()

    with open(outfile, 'wb') as fp:
        for s in a:
            fp.write(str(s) + '\n')


def set_sort(infile, outfile):
    s = blist.sortedset()

    with open(infile, 'rb') as fp:
        for line in fp:
            s.add(int(line))

    with open(outfile, 'wb') as fp:
        for x in s:
            fp.write(str(x) + '\n')


if __name__ == "__main__":
    import timeit

    tstart = timeit.default_timer()
    for i in range(0, 100):
        int_sort('input.txt', 'out_int_sort.txt')
    print "int_sort time elapsed: ", timeit.default_timer() - tstart

    tstart = timeit.default_timer()
    for i in range(0, 100):
        set_sort('input.txt', 'out_set_sort.txt')
    print "set_sort time elapsed: ", timeit.default_timer() - tstart
