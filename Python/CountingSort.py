#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2018 Jared Gillespie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


def counting_sort(arr):
    """Returns a sorted integer list, from a range of values, using Counting Sort algorithm.

    :param arr: The array.

    >>> arr = []
    >>> counting_sort(arr)
    []

    >>> arr = [1]
    >>> counting_sort(arr)
    [1]

    >>> arr = [4, -5, 7, 4, 2, 3, 0]
    >>> counting_sort(arr)
    [-5, 0, 2, 3, 4, 4, 7]

    >>> arr = [5, 4, 3, 2, -1, -9]
    >>> counting_sort(arr)
    [-9, -1, 2, 3, 4, 5]
    """
    if not arr:
        return arr

    smallest, largest = float('inf'), -float('inf')

    for a in arr:
        smallest = min(smallest, a)
        largest = max(largest, a)

    r = largest - smallest + 1

    count = [0] * r
    out = [0] * len(arr)

    for a in arr:
        count[a - smallest] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for a in arr:
        out[count[a - smallest] - 1] = a
        count[a - smallest] -= 1

    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
