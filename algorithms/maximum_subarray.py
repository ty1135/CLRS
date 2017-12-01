import math


def find_maximum(l, low, high):
    if high - low == 1:
        return low, high, l[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_max = find_maximum(l, low, mid)
        right_low, right_high, right_max = find_maximum(l, mid, high)
        cross_low, cross__high, cross_max = find_cross_max(l, low, mid, high)

        if left_max > right_max and left_max > cross_max:
            return left_low, left_high, left_max
        elif right_max > left_max and right_max > cross_max:
            return right_low, right_high, right_max
        else:
            return cross_low, cross__high, cross_max


def find_cross_max(l, low, mid, high):
    left_max = -math.inf
    left_sum = 0
    for i in range(mid-1, low-1, -1):
        left_sum += l[i]
        if left_sum > left_max:
            left_max = left_sum
            left_max_index = i

    right_max = -math.inf
    right_sum = 0
    for i in range(mid, high):
        right_sum += l[i]
        if right_sum > right_max:
            right_max = right_sum
            right_max_index = i

    return left_max_index, right_max_index, left_max + right_max,


if __name__ == "__main__":
    if __name__ == "__main__":
        _input = [3, 4, -1, 7]
        print("input: ", _input)
        output = find_maximum(_input, 0, len(_input))
        print("output: ", output)
