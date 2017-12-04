import random

# hash with chain
# under the assumption of simple uniform hashing
# both unssuccessful and ssucessfule search takes O(1+ n/m) on average
# if n = O(m) ,then search takes O(1) on average


def chained_hash_func(x):
    return x % 100


def chained_hash_insert(table, x):
    # suppose x itself is the key
    slot = chained_hash_func(x)
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
    table = [[] for x in range(100)]

    for x in [random.randint(0, 100) for x in range(200)]:
        chained_hash_insert(table, x)

    for x in table:
        print(x)

    ret = chained_hash_search(table, 50)
    print(ret)