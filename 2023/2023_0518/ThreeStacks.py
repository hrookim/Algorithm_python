class ThreeStacks:
    def __init__(self, stack_size):
        """
        :param stack_size: 각 스택당 사이즈를 의미
        3개의 스택은 순서대로 0, 1, 2라는 고유한 번호를 갖게 된다 
        """
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.pointers = [-1, -1, -1]  # 각 스택의 탑 포인터 변수

    def push(self, stack_num, value):
        if self.pointers[stack_num] == self.stack_size:
            print("Stack Overflow")
            return None
        self.pointers[stack_num] += 1
        index = stack_num * self.stack_size + self.pointers[stack_num]
        self.array[index] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return None
        index = stack_num * self.stack_size + self.pointers[stack_num] - 1
        value = self.array[index]
        self.array[index] = None
        self.pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return None
        index = stack_num * self.stack_size + self.pointers[stack_num] - 1
        return self.array[index]

    def is_empty(self, stack_num):
        return self.pointers[stack_num] == 0


Stacks = ThreeStacks(3)
Stacks.push(0, 1)
Stacks.push(0, 1)
Stacks.push(0, 1)
Stacks.push(0, 1)