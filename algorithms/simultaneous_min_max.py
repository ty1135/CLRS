def smtns_min_max(l):
    if len(l) % 2 == 1:
        l.append(l[0])

    min = max = l[0]
    for i in range(0,len(l), 2):
        if l[i] > l[i+1] and l[i] > max:
            max = l[i]
        elif l[i] <= l[i+1] and l[i] < min:
            min = l[i]
    return min, max


if __name__ == "__main__":
    l = [1,3,5,6234,6345,2134,5,723]
    ret = smtns_min_max(l)
    print(ret)