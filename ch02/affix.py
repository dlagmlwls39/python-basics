num = int(input())

if num >= 1000000000:
    print(str(num // 1000000000) + 'G')
elif num >= 1000000:
    print(str(num // 1000000) + 'M')
elif num >= 1000:
    print(str(num // 1000) + 'k')
else:
    pass
