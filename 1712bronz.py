normal, one, price = map(int,input().split())

if one >= price:
    print(-1)

else:
    k = normal / (price - one)
    k = k + 1
    print(int(k))