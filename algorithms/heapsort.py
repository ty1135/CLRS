def _parent(i):
    return int((i + 1) / 2) -1


def _left(i):
    return 2 * (i + 1) - 1


def _right(i):
    return 2 * (i + 1) + 1 - 1


def _swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


class MaxHeap(list):
    # def __init__(self, heap_size):
    #         super(MaxHeap, self).__init__()
    #         self.heap_size = heap_size

    def max_heapify(self, i):
        l = _left(i)
        r = _right(i)

        largest = i

        if l < self.heap_size and self[l] > self[i]:
            largest = l
        if r < self.heap_size and self[r] > self[largest]:
            largest = r

        if largest != i:
            _swap(self, largest, i)
            self.max_heapify(largest)


    def build_max_heap(self):
        self.heap_size = len(self)
        i = _parent(len(self) - 1)
        for x in range(i, -1, -1):
            self.max_heapify(x)


    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self)-1, -1, -1):
            _swap(self, 0, i)
            self.heap_size -= 1
            self.max_heapify(0)


if __name__ == "__main__":
    l = MaxHeap([16, 4, 10,14, 7, 9, 3, 2, 8, 1])
    l.heap_sort()
    print(l)