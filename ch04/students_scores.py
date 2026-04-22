chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, younghee, yong, minsu]

for scores in students:
    print(scores)

for scores in students:
    sum = 0
    for s in scores:
        sum += s
    avg = sum / 3
    print(scores, sum, avg)
