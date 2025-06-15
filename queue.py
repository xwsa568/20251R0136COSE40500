class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.pop(0) if self._data else None

    def peek(self):
        return self._data[0] if self._data else None

    def is_empty(self):
        return len(self._data) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(q.dequeue())
    print(q.peek())
    print(q.is_empty())
