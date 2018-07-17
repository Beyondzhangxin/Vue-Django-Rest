def get_number(n):
    l1 = range(n+1)[1:]
    l2 = []
    i = 0
    while n:
        l2 += l1[::2]
        l1 = l1[1::2]
        n = n // 2
    return l2


def c(list):
    if list is not None:
        return list[::2]


if __name__ == '__main__':
    print(type(get_number(10)))