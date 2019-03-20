# 用两个队列实现一个栈


class Stock(object):
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.append(node)

    def pop(self):
        if not self.queueA:
            return None
        while len(self.queueA) != 1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop(0)


s = Stock()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())
