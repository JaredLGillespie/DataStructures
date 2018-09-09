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


def radix_sort(arr):
    """Performs an in-place sort of a positive integer list using Radix Sort algorithm.

    :param arr: The array.

    >>> arr = []
    >>> radix_sort(arr)
    >>> arr
    []

    >>> arr = [1]
    >>> radix_sort(arr)
    >>> arr
    [1]

    >>> arr = [4, 71, 4, 2, 32, 0]
    >>> radix_sort(arr)
    >>> arr
    [0, 2, 4, 4, 32, 71]

    >>> arr = [5, 4, 3, 2]
    >>> radix_sort(arr)
    >>> arr
    [2, 3, 4, 5]
    """
    if not arr:
        return

    largest = max(arr)
    exp = 1

    while largest // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def counting_sort(arr, exp):
    n = len(arr)
    out = [0] * n
    count = [0] * 10

    for i in range(n):
        ind = arr[i] // exp
        count[ind % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        ind = arr[i] // exp
        out[count[ind % 10] - 1] = arr[i]
        count[ind % 10] -= 1

    for i in range(n):
        arr[i] = out[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
