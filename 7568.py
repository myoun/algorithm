N = int(input())

people = []

for i in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

grade = []

for i, person in enumerate(people):
    # 덩치가 큰 사람을 구해보자
    bigger = 0
    for p in range(N):
        if people[p][0] > person[0] and people[p][1] > person[1]:
            bigger += 1
    grade.append(bigger + 1)


for g in grade:
    print(g, end=' ')
