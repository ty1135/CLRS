def counting_sort(l, k, key_func):
    """n input elements in the range (0, k)"""
    count_table = [0]*(k + 1)
    for element in l:
        count_table[key_func(element)] += 1

    for index, element in enumerate(count_table):
        if index > 0:
            count_table[index] += count_table[index-1]

    ret = [None] * len(l)
    for i in range(len(l)-1, -1,-1):  # make it stable
        ret[count_table[key_func(l[i])] - 1] = l[i]
        count_table[key_func(l[i])] -= 1

    return ret


if __name__ == "__main__":
    import random

    k = 500
    c = 25

    l = [random.randint(0, k) for x in range(c * k)]
    ret = counting_sort(l, k, lambda x:x)
    print(ret)
