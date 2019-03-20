# 用两个栈实现一个队列


class Queue(object):
    def __init__(self):
        self.stockA = []
        self.stockB = []

    def push(self, node):
        self.stockA.append(node)

    def pop(self):
        if not self.stockB:
            if not self.stockA:
                return None
            else:
                for _ in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())
