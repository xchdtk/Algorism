# FIFO 최대용량이 정해진 큐 클래스
class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() < self.max_size:
            self.stack1.push(item)
            return True
        else:
            return False

    def pop(self):
        try:
            if self.stack2.size() == 0:
                while self.stack1.size() > 0:
                    self.stack2.push(self.stack1.pop())
            finish = self.stack2.pop()
        except IndexError:
            return False
        return finish
n, max_size = map(int, input().strip().split(' '))
my_queue = MyQueue(max_size)
    
for index in range(n):
    input_1 = input().split()
    if "PUSH" in input_1[0]:
        print(my_queue.push(input_1[1]))
    elif 'POP' in input_1[0]:
        print(my_queue.pop())
    else:
        print(my_queue.qsize())