def sort_by_insertion(l):
    for i, key in enumerate(l):
        # add key into the sorted senquence l[0:i]
        j = i - 1
        while j >= 0 and key < l[j]:
            j -= 1
        l.insert(j+1, l.pop(i))
    return l


if __name__ == "__main__":
    _input = [3, 4, 5, 7, 11, 233, 5677, 8, 34, 56, 7]
    print("input: ", _input)
    output = sort_by_insertion(_input)
    print("output: ", output)

