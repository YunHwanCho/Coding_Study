num = int(input())

# 1 6 12 18 24
size = 1
cnt = 1
while num > size:
    size += 6*cnt
    cnt +=1

print(cnt)