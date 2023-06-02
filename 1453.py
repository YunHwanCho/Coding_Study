num = int(input())

man = list(map(int, input().split()))

place = [0] * 101

count = 0

for i in man:
    if place[i] != 0:
        count += 1
    else:
        place[i] += 1

print(count)

