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


def merge_sort(array: list):
    """Sorts a list of items via the merge sort method.

    The ordering of elements is preserved.

    :param array: The list to sort.

    >>> array = []
    >>> merge_sort(array)
    >>> array
    []

    >>> array = [1]
    >>> merge_sort(array)
    >>> array
    [1]

    >>> array = [4, -5, 7, 4, 2, 3, 0]
    >>> merge_sort(array)
    >>> array
    [-5, 0, 2, 3, 4, 4, 7]

    >>> array = [5, 4, 3, 2, -1, -9]
    >>> merge_sort(array)
    >>> array
    [-9, -1, 2, 3, 4, 5]
    """
    if not isinstance(array, list):
        raise ValueError("array must be of type List")

    def divide(array, p, r):
        if p < r:
            q = (p + r) // 2
            divide(array, p, q)
            divide(array, q + 1, r)
            conquer(array, p, q, r)

    def conquer(array, p, q, r):
        left_array = array[p:q+1]
        right_array = array[q+1:r+1]

        i, j = 0, 0
        k = p

        while i <= q - p and j <= r - q - 1:
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i <= q - p:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j <= r - q - 1:
            array[k] = right_array[j]
            j += 1
            k += 1

    divide(array, 0, len(array) - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
