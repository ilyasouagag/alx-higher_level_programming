#!/usr/bin/python3
"""create a linked list"""


class Node:
    """create a node"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get data from linked list"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data to a linked list"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next element of a node in linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next next elemnt of a node in linked list"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """create a sorted linked list"""

    def __init__(self):
        """set head to none to begin with"""
        self.__head = None

    def sorted_insert(self, value):
        """sort elements by data in increasing order"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """print elements of list followed by a new line"""
        new_list = []
        current = self.__head
        while current is not None:
            new_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(new_list)
