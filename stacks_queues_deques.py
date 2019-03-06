#Linear data structures

#Stack: Last-in, first-out
class stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = stack()
s.push(5)
s.push(10)
print(s)