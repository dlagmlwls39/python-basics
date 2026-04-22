def square(x):
    return x ** 2

if __name__ == '__main__':
    # map
    map1 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
    map2 = list(map(square, range(5)))
    print(map1) # [1, 4, 9, 16, 25]
    print(map2) # [0, 1, 4, 9, 16]

    # reduce (결과 누적)
    from functools import reduce
    reduce1 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    reduce2 = reduce(lambda x, y: y + x, 'abcde')
    print(reduce1) # 15
    print(reduce2) # edcba

    # filter
    filterlist = list(filter(lambda x: x < 5, range(10)))
    print(filterlist) # [0, 1, 2, 3, 4]
    odd = list(filter(lambda x: x % 2, range(10))) # 홀수 찾기 (filter에서 거짓(0)은 걸러짐)
    print(odd) # [1, 3, 5, 7, 9]
