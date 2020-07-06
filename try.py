def FindList3MinNum(foo):
    min1, min2, min3 = None, None, None

    for num in foo:
        if min1 is None or min1 > num:
            min1, num = num, min1
        if num is None:
            continue
        if min2 is None or num < min2:
            min2, num = num, min2
        if num is None:
            continue
        if min3 is None or num < min3:
            min3 = num

    return min1, min2, min3

foo = [78, 23, 10, 56, 4, 103, 89, 14]
min1, min2, min3 = FindList3MinNum(foo)
print(min1, min2, min3)