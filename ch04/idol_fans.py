newjeans = ['철수', '영희', '민수', '지현', '서연']
ive = ['영희', '민수', '지수', '서연', '하나']
easpa = ['철수', '지현', '지수', '서연', '나영']

result = []

for fan in newjeans:
    if fan in ive and fan not in easpa:
        result.append(fan)

print(result)
