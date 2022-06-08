def move(x, cur, new, length):
    s = x & (2 ** (cur + length) - 2 ** cur)
    if cur < new:
        return s << (new - cur)
    else:
        return s >> (cur - new)


def main(x):
    res = 0
    res |= move(x, 0, 0, 14)
    res |= move(x, 14, 14, 13)
    res |= move(x, 27, 28, 4)
    res |= move(x, 31, 27, 1)
    return res


print(hex(main(0x5bdf16be)))
