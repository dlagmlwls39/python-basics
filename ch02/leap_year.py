year = int(input())
result = ''

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = '윤년'
        else:
            result = '평년'
    else:    
        result = '윤년'
else:
    result = '평년'

print('출력 연도 {}년은 {}입니다.'.format(year, result))
