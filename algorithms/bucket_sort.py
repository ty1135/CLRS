def bucket_sort(l):
    b = [[] for i in range(len(l))]
    for element in l:
        bucket_index = int(element*(len(l)-1))
        b[bucket_index].append(element)

    ret = []
    for bucket in b:
        bucket.sort()
        ret += bucket

    return ret

if __name__ == "__main__":
    import random
    l = [random.uniform(0,1) for i in range(1000)]
    ret = bucket_sort(l)

    last = ret[0]
    for x in ret:
        assert x >= last
        last = x