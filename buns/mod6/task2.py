class DoubleElement:
    def __init__(self, *lst):
        self.data = lst
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        pair = (self.data[self.index], self.data[self.index + 1] if self.index + 1 < len(self.data) else None)
        self.index += 2
        return pair

    def __iter__(self):
        return self
