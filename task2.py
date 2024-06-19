from collections import deque


class CycleFIFODeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def is_full(self):
        return len(self.buffer) == self.capacity

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def peek(self):
        if self.is_empty():
            return "Buffer is empty"
        return self.buffer[0]

    def __repr__(self):
        return f'CircularBufferDeque(buffer={list(self.buffer)})'


class CycleFIFO:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def add_value(self, value):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def get_front_value(self):
        if self.is_empty():
            return 'FIFO is empty!'
        return self.buffer[self.head]

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

    def show_count(self):
        return f'Count of variables in FIFO: {self.count}'

    def __repr__(self):
        return f'CycleFIFO(buffer={self.buffer}, head={self.head}, tail={self.tail}, count={self.count})'
