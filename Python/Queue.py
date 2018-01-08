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


class Queue:
    """A queue which supports inserting and removing items in a FIFO manner."""

    def __init__(self, elements=None):
        """Instantiates a new instance of a Queue.

        :param elements: Optional. The elements initialize with.
        :exception: TypeError is raised if 'elements' is not iterable.

        >>> my_queue = Queue()
        >>> my_queue
        []

        The front of the queue is the right-most element.
        >>> my_queue = Queue([3, 4, 5])
        >>> my_queue
        [3, 4, 5]
        """
        self._elements = [] if elements is None else [e for e in elements]

    def __contains__(self, item) -> bool:
        return item in self._elements

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self._elements == other._elements
        else:
            return NotImplemented

    def __repr__(self):
        return str(self._elements)

    @property
    def size(self):
        """Returns the size of the queue.

        :return: The size.

        >>> my_queue = Queue()
        >>> my_queue.size
        0

        >>> my_queue = Queue([1, 2, 3])
        >>> my_queue.size
        3
        """
        return len(self._elements)

    def copy(self):
        """Returns a copy of the queue.

        :return: A copy of the queue.

        >>> my_queue = Queue()
        >>> my_queue.copy()
        []

        >>> my_queue = Queue([1, 2, 3])
        >>> my_queue.copy()
        [1, 2, 3]
        """
        return Queue(self._elements[:])

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, otherwise False.

        :return: A boolean indicating whether the queue is empty.

        >>> my_queue = Queue()
        >>> my_queue.is_empty()
        True

        >>> my_queue = Queue([1])
        >>> my_queue.is_empty()
        False
        """
        return len(self._elements) == 0

    def put(self, data):
        """Inserts an element at the end of the queue.

        :param data: The data.

        >>> my_queue = Queue()
        >>> my_queue.put(1)
        >>> my_queue
        [1]

        >>> my_queue = Queue([2, 3, 4])
        >>> my_queue.put(1)
        >>> my_queue
        [1, 2, 3, 4]
        """
        self._elements.insert(0, data)

    def get(self):
        """Retrieves and removes the element at the front of the queue.

        :return: The retrieved data.

        >>> my_queue = Queue([1, 2])
        >>> my_queue.get(), my_queue
        (2, [1])
        """
        if len(self._elements) == 0:
            raise IndexError('queue is empty')

        return self._elements.pop()

    def peek(self):
        """Retrieves the element at the front of the queue.

        :return: The retrieved data.

        >>> my_queue = Queue([1, 2])
        >>> my_queue.peek(), my_queue
        (2, [1, 2])
        """
        if len(self._elements) == 0:
            raise IndexError('queue is empty')

        return self._elements[-1]

    def reverse(self):
        """Reverses the queue.

        >>> my_queue = Queue([1, 2, 3])
        >>> my_queue.reverse()
        >>> my_queue
        [3, 2, 1]
        """
        self._elements[:] = self._elements [::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
