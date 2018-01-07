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

import collections


class Node:
    """A node containing data with, optionally, a pointer to a next node.
    i.e. Node1 -> Node2 OR Node1 -> NULL

    There are no restrictions on what type of data can be contained within the node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next is not None:
            return '%s -> %s' % (self.data, self.next.data)
        else:
            return '%s -> NULL'


class SinglyLinkedList:
    """A list of singly linked nodes containing data.
    i.e. Node1 -> Node2 -> NULL
    """

    def __init__(self, elements=None):
        """Instantiates a new instance of a SinglyLinkedList.

        :param elements: Optional. The elements initialize with.
        :exception: ValueError is raised if 'elements' is not iterable.

        >>> my_list = SinglyLinkedList()
        >>> my_list
        []

        >>> my_list = SinglyLinkedList([3, 4, 5])
        >>> my_list
        [3, 4, 5]
        """
        self._head = None
        self._size = 0
        self._iter_node = None

        if elements is not None:
            self.extend(elements)

    def __add__(self, other):
        if not isinstance(other, SinglyLinkedList):
            raise ValueError("other must be a SinglyLinkedList")

        if self._head is None:
            return other.copy()

        if not len(other):
            return self.copy()

        new_list = self.copy()

        new_list.extend(other)

        return new_list

    def __contains__(self, item) -> bool:
        node = self._head
        while node is not None:
            if node.data == item:
                return True

        return False

    def __delitem__(self, key):
        self.remove_item(key)

    def __eq__(self, other):
        if isinstance(other, SinglyLinkedList):
            if self.size != other.size:
                return False
            else:
                self_node = self._head
                other_node = other._head

                while self_node is not None and other_node is not None:
                    if self_node.data != other_node.data:
                        return False
                    self_node = self_node.next
                    other_node = other_node.next

                return True
        elif isinstance(other, list):
            if self.size != len(other):
                return False

            self_node = self._head
            i = 0

            while self_node is not None:
                if self_node.data != other[i]:
                    return False
                self_node = self_node.next
                i += 1

            return True
        else:
            return NotImplemented

    def __getitem__(self, index: int):
        return self.get(index)

    def __iadd__(self, other):
        self.extend(other)

    def __iter__(self):
        return self

    def __len__(self):
        return self._size

    def __next__(self):
        if self._head is None:
            raise StopIteration()

        if self._iter_node is None:
            self._iter_node = self._head
        else:
            self._iter_node = self._iter_node.next

            if self._iter_node is None:
                raise StopIteration()

        return self._iter_node.data

    def __reversed__(self):
        """Returns a reversed copy of the list.

        :return: A reversed copy of the list.

        >>> my_list = SinglyLinkedList([1, 2, 3])
        >>> list(reversed(my_list))
        [3, 2, 1]
        """
        copy = self.copy()
        copy.reverse()

        for data in copy:
            yield data

    def __repr__(self):
        s = []
        node = self._head
        while node is not None:
            s.append(node.data)
            node = node.next

        return str(s)

    @property
    def size(self) -> int:
        """Returns the size of the list.

        :return: The size.

        >>> my_list = SinglyLinkedList()
        >>> my_list.size
        0

        >>> my_list = SinglyLinkedList([1, 2, 3])
        >>> my_list.size
        3
        """
        return self._size

    def append(self, data):
        """Appends the data to the end of the list.

        :param data: The data to append.

        >>> my_list = SinglyLinkedList()
        >>> my_list.append(5)
        >>> my_list
        [5]

        >>> my_list = SinglyLinkedList([3, 4])
        >>> my_list.append(1)
        >>> my_list
        [3, 4, 1]
        """
        self._size += 1

        if self._head is None:
            self._head = Node(data)
        else:
            node = self._head
            while node.next is not None:
                node = node.next
            node.next = Node(data)

    def copy(self):
        """Returns a copy of the list.

        :return: A copy of the list.

        >>> my_list = SinglyLinkedList()
        >>> my_list.copy()
        []

        >>> my_list = SinglyLinkedList([5, 7, -1])
        >>> my_list.copy()
        [5, 7, -1]
        """
        list_copy = SinglyLinkedList()

        node = self._head
        while node is not None:
            list_copy.append(node.data)
            node = node.next

        return list_copy

    def extend(self, other):
        """Extends the list with the elements of another.

        :param other: A list or SinglyLinkedList to extend the list with.
        :exception: ValueError is raised if 'other' is not iterable.

        >>> my_list = SinglyLinkedList([1])
        >>> my_list.extend([2, 3, 4])
        >>> my_list
        [1, 2, 3, 4]
        """
        if isinstance(other, collections.Iterable):
            if self._head is None:
                added_head = False
                node = None

                for data in other:
                    if not added_head:
                        self._head = Node(data)
                        node = self._head
                        added_head = True
                    else:
                        node.next = Node(data)
                        node = node.next
                    self._size += 1
            else:
                tail = self._head
                while tail.next is not None:
                    tail = tail.next

                for data in other:
                    tail.next = Node(data)
                    tail = tail.next
                    self._size += 1
        else:
            raise ValueError("other must be iterable")

    def get(self, index: int):
        """Gets the data at the specified index.

        :param index: The index to retrieve.
        :return: The data.
        :exception: IndexError is raised if index is out of bounds.

        >>> my_list = SinglyLinkedList()
        >>> my_list.extend([4, 6, 2])
        >>> my_list.get(1)
        6

        >>> my_list = SinglyLinkedList()
        >>> my_list.extend([5, 2, -1, 2])
        >>> my_list.get(-2)
        -1
        """
        if index < -self.size or index >= self.size:
            raise IndexError("index is out of range")

        if index < 0:
            index = self.size + index

        node = self._head
        for i in range(index):
            node = node.next

        return node.data

    def insert(self, index: int, data):
        """Inserts the data at the given element.
        If an element exists at the given position, the element is inserted before it.

        :param index: The index to insert at.
        :param data: The data to insert.
        :exception: IndexError is raised if index is out of bounds.

        >>> my_list = SinglyLinkedList()
        >>> my_list.insert(0, 3)
        >>> my_list.insert(0, 1)
        >>> my_list.insert(-1, 2)
        >>> my_list.insert(len(my_list), 4)
        >>> my_list
        [1, 2, 3, 4]
        """
        if index < -self.size or index > self.size:
            raise IndexError("index is out of range")

        if index < 0:
            index = self.size + index

        if self._head is None:
            self._head = Node(data)
        elif index == 0:
            head = self._head
            self._head = Node(data)
            self._head.next = head
        else:
            next_node = self._head
            prev_node = None
            for i in range(index):
                prev_node = next_node
                next_node = next_node.next

            new_node = Node(data)
            prev_node.next = new_node
            new_node.next = next_node

        self._size += 1

    def is_empty(self):
        """Returns True if the list is empty, otherwise False.

        :return: A boolean indicating whether the list is empty.

        >>> my_list = SinglyLinkedList()
        >>> my_list.is_empty()
        True

        >>> my_list = SinglyLinkedList([1])
        >>> my_list.is_empty()
        False
        """
        return self._size == 0

    def pop(self):
        """Removes and returns the data from the beginning of the list.

        :return: The data.
        :exception: IndexError is raised if list is empty.

        >>> my_list = SinglyLinkedList([1, 2, 3])
        >>> my_list.pop()
        1
        """
        if self._head is None:
            raise IndexError("list is empty")

        head = self._head
        self._head = head.next

        # Update iterable ptr
        if self._iter_node == head:
            self._iter_node = self._head

        self._size -= 1

        return head.data

    def pop_last(self):
        """Removes and returns the data from the beginning of the list.

        :return: The data.
        :exception: IndexError is raised if list is empty.

        >>> my_list = SinglyLinkedList([1, 2, 3])
        >>> my_list.pop_last()
        3
        """
        if self._head is None:
            raise IndexError("list is empty")

        next_node = self._head
        prev_node = None

        while next_node.next is not None:
            prev_node = next_node
            next_node = next_node.next

        prev_node.next = None

        return next_node.data

    def prepend(self, data):
        """Prepends the data to the end of the list.

         :param data: The data to append.

         >>> my_list = SinglyLinkedList()
         >>> my_list.prepend(5)
         >>> my_list
         [5]

         >>> my_list = SinglyLinkedList([3, 4])
         >>> my_list.prepend(1)
         >>> my_list
         [1, 3, 4]
         """
        self._size += 1

        head = self._head

        self._head = Node(data)
        self._head.next = head

    def remove(self, index: int):
        """Removes and returns the data at the given index.

         :param index: The index to remove.
         :return: The data at the index.
         :exception: IndexError is raised if index is out of bounds.

         >>> my_list = SinglyLinkedList([4, 7, 2])
         >>> my_list.remove(0)
         4

         >>> my_list = SinglyLinkedList([3, 4])
         >>> my_list.remove(-1)
         4
         """
        if index < -self.size or index >= self.size or self._head is None:
            raise IndexError("index is out of range")

        if index < 0:
            index = self.size + index

        if index == 0:
            head = self._head
            self._head = self._head.next

            # Update iterable ptr
            if self._iter_node == head:
                self._iter_node = self._head

            self._size -= 1
            return head.data
        else:
            next_node = self._head
            prev_node = None
            for i in range(index):
                prev_node = next_node
                next_node = next_node.next

            prev_node.next = next_node.next

            # Update iterable ptr
            if self._iter_node == next_node:
                self._iter_node = next_node.next

            self._size -= 1
            return next_node.data

    def remove_item(self, data):
        """Removes the first occurrence of the given data.

         :param data: The data to remove.
         :exception: ValueError is raised if item is not found.

         >>> my_list = SinglyLinkedList([4, 7, 2])
         >>> my_list.remove_item(7)
         >>> my_list
         [4, 2]

         >>> my_list = SinglyLinkedList([3, 4, 3])
         >>> my_list.remove_item(3)
         >>> my_list
         [4, 3]
         """
        if self._head is None:
            raise ValueError("item not found")

        if self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return

        next_node = self._head
        prev_node = None

        while next_node is not None:
            if next_node.data == data:
                if prev_node is not None:
                    prev_node.next = next_node.next

                # Update iterable ptr
                if self._iter_node == next_node:
                    self._iter_node = prev_node.next

                self._size -= 1
                return

            prev_node = next_node
            next_node = next_node.next

        raise ValueError("item not found")

    def reverse(self):
        """Reverses the list.

        >>> my_list = SinglyLinkedList([1, 2, 3])
        >>> my_list.reverse()
        >>> my_list
        [3, 2, 1]
        """
        prev_prev_node = None
        prev_node = None
        next_node = self._head

        while next_node is not None:
            prev_prev_node = prev_node
            prev_node = next_node
            next_node = next_node.next

            prev_node.next = prev_prev_node

        self._head = prev_node
        a = 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

