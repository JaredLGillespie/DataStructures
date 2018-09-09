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


def binary_search(arr, v):
    """Searches for whether an element exists in the list using Binary Search.

    :param arr: The array.

    >>> arr = []
    >>> binary_search(arr, 1)
    False

    >>> arr = [1, 2, 3]
    >>> binary_search(arr, 2)
    True

    >>> arr = [-6, 1, 1, 2, 3, 4, 4, 5, 15, 28, 31, 34, 34]
    >>> binary_search(arr, 4)
    True

    >>> arr = [3, 4, 8]
    >>> binary_search(arr, 9)
    False

    >>> arr = [-1, 0, 2]
    >>> binary_search(arr, -1)
    True

    >>> arr = [-1, 0, 2]
    >>> binary_search(arr, -2)
    False
    """
    if not arr:
        return False

    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == v:
            return True
        elif arr[m] < v:
            l = m + 1
        else:
            r = m - 1

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
