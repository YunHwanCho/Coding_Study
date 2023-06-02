x, y, w, h = map(int, input().split())

small = min(x , y , w-x, h-y)

print(small)

