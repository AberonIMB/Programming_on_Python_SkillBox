class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        if self.end is None:
            raise IndexError
        else:
            val = self.end
            self.end = val.pref
            return val.data

    def push(self, val):
        node = Node(val)
        node.pref = self.end
        self.end = node

    def print(self):
        current_node = self.end
        while current_node:
            print(current_node.data, end='>')
            current_node = current_node.pref
        print('Empty')