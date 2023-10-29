class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def get_size(self):
        current_node = self.start
        count = 0
        while current_node:
            count += 1
            current_node = current_node.nref
        return count

    def pop(self):
        if self.start is None:
            raise IndexError
        else:
            val = self.start
            self.start = val.nref
            return val.data

    def push(self, val):
        node = Node(val)
        if self.start is None:
            self.start = self.end = node
        else:
            self.end.nref = node
            node.pref = self.end
            self.end = node

    def insert(self, n, val):
        if n < 0 or n > self.get_size() - 1:
            raise IndexError

        node = Node(val)
        if n == 0:
            node.nref = self.start
            self.start.pref = node
            self.start = node
        else:
            count = 0
            current_node = self.start
            while count != n - 1:
                count += 1
                current_node = current_node.nref

            node.pref = current_node
            node.nref = current_node.nref
            current_node.nref.pref = node
            current_node.nref = node

    def print(self):
        current_node = self.start
        while current_node:
            print(current_node.data, end='>')
            current_node = current_node.nref
        print('None')