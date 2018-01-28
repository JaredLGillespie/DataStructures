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


class Node:
    """A node containing a key and value with, optionally, a pointer to a next and/or previous node.
    i.e. Node1 <-> Node2 OR NULL <- Node1 -> NULL

    There are no restrictions on what type of data can be contained within the node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        if self.prev is None:
            if self.next is None:
                return 'NULL -> (%s:%s) -> NULL' % (self.key, self.value)
            return 'NULL -> (%s:%s) -> (%s:%s)' % (self.key, self.value,
                                                   self.next.key, self.next.value)
        elif self.next is None:
            return '(%s:%s) -> (%s:%s) -> NULL' % (self.prev.key, self.prev.value,
                                                   self.key, self.value)
        return '(%s:%s) -> (%s:%s) -> (%s:%s)' % (self.prev.key, self.prev.value,
                                                  self.key, self.value,
                                                  self.next.key, self.value)


class LRUCache:
    """A Least-Recently-Used (LRU) cache which supports retrieving and adding items in constant time.

    If the capacity is exceeded upon adding an item, the least recently used item is evicted from the cache.
    If an item is retrieved from the cache, it is the most recently used item in the cache.

    >>> cache = LRUCache(3)
    >>> cache.put(1, "A")
    >>> cache.put(2, "B")
    >>> cache.put(4, "C")
    >>> cache.put(3, "D")
    >>> cache.remove(2)
    >>> cache.get(4), cache
    ('C', ['4:C', '3:D'])
    """

    def __init__(self, capacity: int):
        """Instantiates a new instance of a LRUCache.

        :param capacity: The size of the cache.
        :exception: ValueError is raised if 'capacity' is < 1.

        >>> cache = LRUCache(1)
        >>> cache
        []

        >>> cache = LRUCache(1)
        >>> cache.put(1, "thing")
        >>> cache
        ['1:thing']
        """
        if capacity < 0:
            raise ValueError("capacity must be > 0")

        self._capacity = capacity
        self._size = 0
        self._cache_head = None
        self._cache_tail = None
        self._map = dict()

    def __contains__(self, key) -> bool:
        return key in self._map

    def __delitem__(self, key):
        self.remove(key)

    def __eq__(self, other):
        if isinstance(other, LRUCache):
            return self._map == other._map
        elif isinstance(other, list):
            return NotImplemented

    def __len__(self):
        return self._size

    def __repr__(self):
        s = []
        node = self._cache_head
        while node is not None:
            s.append('%s:%s' % (node.key, node.value))
            node = node.next

        return str(s)

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self) -> int:
        """Returns the number of elements in the cache.

        :return: The size.

        >>> cache = LRUCache(1)
        >>> cache.size
        0

        >>> cache = LRUCache(2)
        >>> cache.put(1, "value")
        >>> cache.put(2, "other")
        >>> cache.size
        2
        """
        return self._size

    def get(self, key):
        """Retrieves and element from the cache.
        This element becomes the most recently used.

           :return: The retrieved data.

           >>> cache = LRUCache(2)
           >>> cache.put(1, "A")
           >>> cache.put(2, "B")
           >>> cache.get(1), cache
           ('A', ['1:A', '2:B'])
           """
        if key in self._map:
            node = self._map[key]

            if node != self._cache_head:
                self._remove_cache(node)
                self._append_cache(node)

            return node.value
        else:
            return None

    def put(self, key, value):
        """Inserts an element into the cache.
        This element becomes the most recenlty used.

        :param data: The data.

        >>> cache = LRUCache(1)
        >>> cache.put(1, "A")
        >>> cache
        ['1:A']

        >>> cache = LRUCache(3)
        >>> cache.put(1, "A")
        >>> cache.put(2, "B")
        >>> cache.put(4, "C")
        >>> cache
        ['4:C', '2:B', '1:A']
        """
        if key in self._map:
            node = self._map[key]

            if node != self._cache_head:
                self._remove_cache(node)
                self._append_cache(node)
        else:
            if self._capacity == self._size:
                self._remove_cache(self._cache_tail)

            node = Node(key, value)

            self._map[key] = node
            self._append_cache(node)

    def is_empty(self):
        """Returns True if the cache is empty, otherwise False.

        :return: A boolean indicating whether the cache is empty.

        >>> cache = LRUCache(1)
        >>> cache.is_empty()
        True

        >>> cache = LRUCache(1)
        >>> cache.put(1, 'A')
        >>> cache.is_empty()
        False
        """
        return self._size == 0

    def remove(self, key):
        """Removes data from the cache, if it exists.

           :param data: The data to remove.

           >>> cache = LRUCache(2)
           >>> cache.put(1, "hi")
           >>> cache.put(2, "bye")
           >>> cache.remove(1)
           >>> cache
           ['2:bye']

           >>> cache = LRUCache(1)
           >>> cache.remove("doesn't exist")
           >>> cache
           []
           """
        if key in self._map:
            node = self._map[key]
            self._map.pop(key)
            self._remove_cache(node)

    def _append_cache(self, node: Node):
        self._size += 1

        if self._cache_head is None:
            self._cache_head = node
            self._cache_tail = node
        else:
            head = self._cache_head

            self._cache_head = node
            self._cache_head.next = head
            self._cache_head.next.prev = self._cache_head

    def _remove_cache(self, node: Node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node == self._cache_head:
            self._cache_head = node.next

        if node == self._cache_tail:
            self._cache_tail = node.prev

        self._size -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

