def triple(x):
    if x.isdigit():
        return int(x) * 3
    else:
        return x * 3

def korean_age(y):
    from datetime import datetime
    today = datetime.today()
    return today.year - int(y) + 1

if __name__ == '__main__':
    x = input()
    print(triple(x))
    y = input('태어난 연도 입력: ')
    print('힌국 나이:', korean_age(y))
