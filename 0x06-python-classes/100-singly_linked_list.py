#!/usr/bin/python3
"""create a linked list"""


class Node:
    """create a node"""

    def __init__(self, data, next_node=None):
        """attributes of node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next"""
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """create a sorted linked list"""

    def __init__(self):
        """set head to none"""
        self.__head = None

    def sorted_insert(self, value):
        """sort elements"""
        new = Node(value)
        current = self.__head
        prev = None
        if self.__head == None:
            self.__head = new
        else:
            while (current != None):
                if value < current.data:
                    break
                prev = current
                current = current.next_node
            new.next_node = current
            if prev == None:
                self.__head = new
            else:
                prev.next_node = new

    def __str__(self):
        """print elements of list"""
        new_list = []
        current = self.__head
        while (current != None):
            new_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(new_list)
