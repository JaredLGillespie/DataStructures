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


def quick_sort(arr):
    """Sorts the list in-place using Bubble Sort algorithm.

    :param arr: The array.

    >>> arr = []
    >>> quick_sort(arr)
    >>> arr
    []

    >>> arr = [1]
    >>> quick_sort(arr)
    >>> arr
    [1]

    >>> arr = [4, -5, 7, 4, 2, 3, 0]
    >>> quick_sort(arr)
    >>> arr
    [-5, 0, 2, 3, 4, 4, 7]

    >>> arr = [5, 4, 3, 2, -1, -9]
    >>> quick_sort(arr)
    >>> arr
    [-9, -1, 2, 3, 4, 5]
    """
    if not arr:
        return arr

    divide(arr, 0, len(arr) - 1)


def divide(arr, l, r):
    index = partition(arr, l, r)
    if l < index - 1:
        divide(arr, l, index - 1)

    if index < r:
        divide(arr, index, r)


def partition(arr, l, r):
    pivot = arr[(l + r) // 2]

    while l <= r:
        while arr[l] < pivot:
            l += 1

        while arr[r] > pivot:
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    return l


if __name__ == '__main__':
    import doctest
    doctest.testmod()
