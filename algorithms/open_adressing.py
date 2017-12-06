# probe positions are offset by h2(key) mod m
# hence ,h2(k) must be relatively prime to m

# 1. m = prime ; h2 = 1 + [k mod (m-1)]
# 2. m = 2^p ; h2 = odd    seems more practical to me

import random


def double_hash(key, i):
    def auxiliary_hash_1(k):
        return k % 1024

    def auxiliary_hash_2(k):
        return (k * 2 + 1) % 1024

    return (auxiliary_hash_1(key) + i * auxiliary_hash_2(key)) % 1024


def insert(table, x):
    key = x
    for i in range (0,1024):
        slot = double_hash(key, i)
        if table[slot] is None:
            table[slot] = x
            return
    else:
        raise Exception("overflow")


def search(table, x):
    key = x
    for i in range (0,1024):
        slot = double_hash(key, i)
        if table[slot] is None:
            break
        elif table[slot] == x:
            return x


if __name__ == "__main__":
    table = [None] * 1024

    for x in [random.randint(0, 1000) for x in range(1024)]: # changing it to 1025 will raise proves correctness^ ^
        insert(table, x)
        print(table)

    ret = search(table, 999)
    print(ret)
