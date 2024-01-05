class Array(object):
    def __init__(self, capacity, fillValue=None):
        self.items = list()
        self.logicalSize = 0
        self.capacity = capacity
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def size(self):
        return self.logicalSize

    def insert(self, index, val):
        # if Array if full increate the capacity
        if self.logicalSize == self.capacity:
            for _ in range(self.capacity):
                self.items.append(self.fillValue)
            self.capacity *= 2

        if index >= self.logicalSize:
            self.items[self.logicalSize] = val
        else:
            for i in range(self.logicalSize, index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = val

        self.logicalSize += 1

    def pop(self, index):
        if 0 > index or index > self.logicalSize:
            return

        remove = self.items[index]

        for i in range(index, self.logicalSize - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.logicalSize - 1] = self.fillValue

        self.logicalSize -= 1
        return remove


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)
    for item in range(4):
        a.insert(0, item)
    print("Items:", a)
    a.insert(1, 77)
    print("Items:", a)
    a.insert(10, 10)
    print("Items:", a)
    print(a.pop(3))
    print("Items:", a)
    for count in range(5):
        print(a.pop(0), end=" ")
    print()


if __name__ == "__main__":
    main()