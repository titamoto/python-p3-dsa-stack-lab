class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return self.items

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        return False

    def search(self, target):
        if target in self.items:
            i = len(self.items) -1
            while i >= 0:
                if self.items[i] == target:
                    return len(self.items) -1 -i
                i -= 1
        return -1
