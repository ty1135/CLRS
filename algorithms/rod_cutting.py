import math

def cut_rod(prices, n):
    if n == 0:
        return 0

    q = -math.inf
    for i in range(1, n+1):
        q = max(q, prices[i]+cut_rod(prices, n-i))
    return q


def bottom_up_cut_rod(prices, n):
    r = [None] * (n+1)
    r[0] = 0

    for i in range(1, n+1):
        q = -math.inf
        for j in range(1, i+1):
            q = max(q, prices[j] + r[i-j])
        r[i] = q

    return r[n]


if __name__ == "__main__":
    prices = (None, 1, 5, 8, 9, 10,17, 17, 20, 24, 30)

    for i in range(0, 10):
        ret1 = cut_rod(prices, i+1)
        print(ret1)

        ret2 = bottom_up_cut_rod(prices, i+1)
        print(ret2)