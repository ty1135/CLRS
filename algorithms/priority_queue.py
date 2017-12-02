import math

from heapsort import MaxHeap


def _parent(i):
    return int((i + 1) / 2) -1

def _swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


class PriorityQueue(MaxHeap):
    def heap_maximum(self):
        return self[0]

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise Exception("heap underflow")

        max = self[0]
        self[0] = self[self.heap_size-1]
        self[self.heap_size - 1] = max
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i, key):
        if key < self[i]:
            raise Exception("new key is smaller than current key")
        self[i] = key
        while _parent(i) >= 0 and self[_parent(i)] < self[i]:
            _swap(self, i, _parent(i))
            i = _parent(i)

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.append(None)
        self[self.heap_size-1] = -math.inf

        self.heap_increase_key(self.heap_size-1, key)


if __name__ == "__main__":
    l = PriorityQueue([16, 4, 10,14, 7, 9, 3, 2, 8, 1])
    l.build_max_heap()
    l.heap_increase_key(3, 1000)
    print(l)
    print(l.heap_maximum())
    l.max_heap_insert(2000)
    print(l)
    print("start extracting")
    while True:
        print(l.heap_extract_max())

