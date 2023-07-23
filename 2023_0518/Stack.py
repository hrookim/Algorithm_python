class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1  # 없다. 

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):  # return은 필요가 없다.
        if self.is_full():
            raise ValueError('Stack Overflow!')
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):  # return은 있으나, 인자는 필요가 없다.
        if self.is_empty():
            raise ValueError('Empty Stack. Nothing to pop.')
        else:
            item = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Empty Stack. Nothing to peek.')
        else:
            return self.items[self.top]

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result


s1 = Stack(10)  # size가 10인 stack을 생성한다.
s1.is_empty()  # True
s1.push(1)
s1.is_empty()  # False
s1.push(2)
s1.push(3)
s1.peek()  # 3
s1.push(4)
s1.is_full()  # False
s1.push(5)
s1.is_full()  # True
s1.pop()  # 5
print(s1)  # stack size & 내용물 확인

