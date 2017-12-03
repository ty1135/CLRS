from counting_sort import counting_sort

def radix_sort(l, k):
    for i in range(k):
        key_func = lambda x: int(x/(10**i)) % 10
        l = counting_sort(l, 10, key_func)
        print(l)
    return l


if __name__ == "__main__":
    import random
    l = [random.randint(100, 999) for x in range(20)]
    ret = radix_sort(l, 3)
    print(ret)