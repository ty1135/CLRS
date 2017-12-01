import math


def merge(l0, p, q, r):
    l1 = l0[p:q] + [math.inf]
    l2 = l0[q:r] + [math.inf]
    i = j = 0
    for k in range(p, r):
        if l1[i] < l2[j]:
            l0[k] = l1[i]
            i += 1
        else:
            l0[k] = l2[j]
            j += 1


def merge_sort(l, p, r):
    if r - p > 1:
        q = int((p + r) / 2)
        merge_sort(l, p, q)
        merge_sort(l, q, r)
        merge(l, p, q, r)


if __name__ == "__main__":
    _input = [3, 4, 5, 7, 11, 233, 5677, 8, 34, 56, 7]
    print("input: ", _input)
    merge_sort(_input, 0, len(_input))
    print("output: ", _input)
