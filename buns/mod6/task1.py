class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def get(self, index):
        if index < 0:
            raise IndexError
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                raise IndexError
            current_node = current_node.next
        if current_node:
            return current_node.data
        else:
            raise IndexError

    def remove(self, index):
        if index < 0 or not self.head:
            raise IndexError()
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            pre_node = self.head
            for i in range(index + 1):
                if current_node is None:
                    raise IndexError()
                if i == index - 1:
                    pre_node = current_node
                current_node = current_node.next
            pre_node.next = current_node

    def insert(self, n, val):
        new_node = Node(val)
        if n < 0:
            raise IndexError
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            pre_node = self.head
            for i in range(n):
                if current_node.next is None:
                    raise IndexError
                if i == n - 1:
                    pre_node = current_node
                current_node = current_node.next
            pre_node.next = new_node
            new_node.next = current_node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next
