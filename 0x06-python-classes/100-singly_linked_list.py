#!/usr/bin/python3
"""Defines a singly linked list"""


class Node():
    """Class that defines a node"""

    def __init__(self, data, next_node=None):
        """Method for initialize a Node object.

        Args:
            data(int): Integer to insert inside the store inside node.
            next_node(Atributte): Atributte that store a Node object.

        Returns:
            Always nothing.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter of data.

        Args:
           Any Arguments.

        Returns:
           The current value of data.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter of data.

        Args:
           value(int): Integer store inside node.

        Return:
           Always nothing.

        """
        if isinstance(value, int) is not True:
                raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter of next_node.

        Args:
           Any Arguments.

        Returns:
           The current value of data.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter of next_node.

        Args:
           value(atributte): Atributte that store a Node object.

        Return:
           Always nothing.

        """
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList():
    """Class that defines a singly linked list"""

    def __init__(self):
        """Method for initialize a single list object with head.

        Args:
           Any arguments.

        Returns:
           Always nothing.

        """
        self.__head = None

    def sorted_insert(self, value):
        """Method to manage a insert new node into the list.

        Args:
           value(data): Integer to store inside node.

        Returns:
           Always nothing.

        """
        new_node = Node(value, None)
        tmp = self.__head
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Method to print Square instance.
        Args:
            No Arguments
        Return:

        """
        node_data = ""
        if self.__head is None:
            return ""
        else:
            tmp = self.__head
            while tmp is not None:
                node_data += str(tmp.data) + "\n"
                tmp = tmp.next_node
        return node_data[:-1]
