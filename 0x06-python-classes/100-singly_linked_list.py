#!/usr/bin/python3
"""
    Node: Header for a singly linked list
"""


class Node:
    """
        A Node for singly linked list to add an element in a sorted list
        Attr:
            __data: a private attribute that contains the data of the
                linked node
            __next_node: a private attribute that has the instance of
                the next node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ A getter method for data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ A setter method for data attribute """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ A getter method for next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ A setter method for next_node attribute """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""
    SinglyLinkedList: a singly linked list class to linked data
        with the address of each corresponding node in the list
"""


class SinglyLinkedList:
    """
        A singly Linked list class to store both data and node
            address of the list.

        Attr:
            __head: a private attribute that keep the instance
                of the corresponding class.
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ A method that sort before inserting into the list """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ A method that Prints an instance of a class like a string """
        if self.__head is None:
            return ""

        current = self.__head
        linked_list = ""
        while current is not None:
            linked_list += str(current.data) + "\n"
            current = current.next_node
        return linked_list.strip()
