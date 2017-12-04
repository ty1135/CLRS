class Queue(list):
    def __init__(self, *args, **kwargs):
        super(Queue, self).__init__(*args, **kwargs)
        self.tail = 0
        self.head = 0
        self.empty = True

    def enqueue(self, x):
        if self.tail == self.head and not self.empty:
            raise Exception("overflow")
        else:
            self[self.tail] = x
            self.tail = (self.tail + 1) % len(self)
            self.empty = False


    def dequeue(self):
        if self.empty:
            raise Exception("underflow")
        else:
            ret = self[self.head]
            self.head = (self.head + 1) % len(self)

        if self.tail == self.head:
            self.empty = True

        return ret


if __name__ == "__main__":
    q = Queue([0]*3)
    print(q)

    q.enqueue('x1')
    q.enqueue('x2')
    q.enqueue('x3')

    print(q)

    ret = q.dequeue()
    print(ret)
    print(q)

    ret = q.dequeue()
    print(ret)

    ret = q.dequeue()
    print(ret)