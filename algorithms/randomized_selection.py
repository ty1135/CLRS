from quicksort import partition


def order_select(l, p, r, i):
    # no randomization implemented here
    if p == r:
        return l[p]

    index = i - 1
    pivot_index = partition(l, p, r)
    if index == pivot_index:
        return l[pivot_index]

    if index > pivot_index:
        return order_select(l, pivot_index+1, r, index-pivot_index)
    else:
        return order_select(l, p, pivot_index-1, i)


if __name__ == "__main__":
    l = [1,23,5,6,243,123123]
    print(order_select(l, 0, len(l)-1, 1))