import random

# hash with chain
# under the assumption of simple uniform hashing
# both unssuccessful and ssucessfule search takes O(1+ n/m) on average
# if n = O(m) ,then search takes O(1) on average


def chained_hash_func(x):
    # division method
    # choose a prime around m
    return x % 103

def chained_hash_func_alternative(x):
    # multiplication method
    constant = (5 ** 0.5 - 1) / 2
    fraction = x * constant - int(x * constant)
    return int(fraction * 103) # normally m 103 is chose to be power of 2 instead of 103

def chained_hash_insert(table, x):
    # suppose x itself is the key
    #slot = chained_hash_func(x)
    slot = chained_hash_func_alternative(x)
    table[slot].append(x)


def chained_hash_search(table, x):
    # suppose x itself is the key
    slot = chained_hash_func(x)
    try:
        index = table[slot].index(x)
        return table[slot][index]
    except ValueError:
        return None



if __name__ == "__main__":
    table = [[] for x in range(104)]

    for x in [random.randint(0, 10000) for x in range(200)]:
        chained_hash_insert(table, x)

    for x in table:
        print(x)

    ret = chained_hash_search(table, 50)
    print(ret)