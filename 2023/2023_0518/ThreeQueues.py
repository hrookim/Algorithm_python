class ThreeQueues:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.array = [None] * (queue_size * 3)
        self.fronts = [0, queue_size, queue_size * 2]
        self.rears = [0, queue_size, queue_size * 2]

    def enqueue(self, queue_num, value):
        if self.is_full(queue_num):
            raise Exception("Queue is full")
        self.array[self.rears[queue_num]] = value
        self.rears[queue_num] = (self.rears[queue_num] + 1) % (self.queue_size * 3)

    def dequeue(self, queue_num):
        if self.is_empty(queue_num):
            raise Exception("Queue is empty")
        value = self.array[self.fronts[queue_num]]
        self.array[self.fronts[queue_num]] = None
        self.fronts[queue_num] = (self.fronts[queue_num] + 1) % (self.queue_size * 3)
        return value

    def peek(self, queue_num):
        if self.is_empty(queue_num):
            return None
        return self.array[self.fronts[queue_num]]

    def is_empty(self, queue_num):
        return self.fronts[queue_num] == self.rears[queue_num]

    def is_full(self, queue_num):
        return (self.rears[queue_num] + 1) % (self.queue_size * 3) == self.fronts[queue_num]

    def size(self, queue_num):
        if self.rears[queue_num] >= self.fronts[queue_num]:
            return self.rears[queue_num] - self.fronts[queue_num]
        return self.queue_size * 3 - self.fronts[queue_num] + self.rears[queue_num]


Q = ThreeQueues(3)
Q.enqueue(0, 1)
Q.enqueue(0, 2)
Q.dequeue(0)
Q.enqueue(0, 3)
Q.dequeue(0)
Q.enqueue(0, 4)
print(Q.array)
