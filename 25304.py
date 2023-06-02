total = int(input())
num = int(input())
price = 0
for _ in range(num):
    i , y = map(int, input().split())
    
    price += i*y


if price == total:
    print("Yes")
else:
    print("No")
    







    
