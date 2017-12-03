"""
Bug detected, not fixed yet
"""


def _swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


def partition(l, low, high, value):
    print("-")
    print(l, low, high, value)
    # partition by 'value' instead of object,
    # do 'replacement'

    i = low
    pivot = None
    for x in range(low, high+1):
        if l[x] <= value:
            if l[x] == value:
                pivot = x
            _swap(l, i, x)
            i += 1
    _swap(l, i-1, pivot)
    return i - 1  # last element index in <= partition


def median(l):
    l.sort()
    return l[int(len(l)/2)]


def select(l, i):
    if len(l) == 1:
        return l[0]

    index = 0
    medians = []

    while index < len(l):
        group = l[index: index+5]
        median_of_group = median(group)
        medians.append(median_of_group)
        index += 5

    median_of_medians = select(medians, int(len(medians)/2))

    last_el_index = partition(l, 0, len(l)-1, median_of_medians)

    if i < last_el_index + 1:
        return select(l[:last_el_index], i)
    elif i > last_el_index + 1:
        return select(l[last_el_index+1:], i-last_el_index-1)
    else:
        return l[last_el_index]



if __name__ == "__main__":
    l = [3, 237, 4324, 5, 11142, 2343, 435677, 8, 34, 52346, 6434]
    ret = (select(l , 6))
    print("ret", ret)




