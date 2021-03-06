#!/usr/bin/env python3
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


def insertion_sort(arr):
    """Sorts the list in-place using Bubble Sort algorithm.

    :param arr: The array.

    >>> arr = [1, 2, 3]
    >>> insertion_sort(arr)
    >>> print(arr)
    [1, 2, 3]

    >>> arr = [3, 2, 5, 4, 4, 0]
    >>> insertion_sort(arr)
    >>> print(arr)
    [0, 2, 3, 4, 4, 5]

    """
    for i in range(len(arr)):
        min_val, min_index = None, -1
        for j in range(i, len(arr)):
            if min_val is None or arr[j] < min_val:
                min_val, min_index = arr[j], j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
