num = int(input())

for i in range(num,0,-1):
    print(" " * (i-1),end = '')
    print("*" * (2 * (num - i + 1)-1 ))

