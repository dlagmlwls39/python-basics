def compare(a, b):
    if a > b:
        print(f'{a} > {b}')
    elif a < b:
        print(f'{a} < {b}')
    else:
        print(f'{a} == {b}')

if __name__ == '__main__':
    a, b = map(int, input().split())
    compare(a, b)
