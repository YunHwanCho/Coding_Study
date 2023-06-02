num = int(input())
cnt = 0
numbers = list(map(int,input().split()))
print(numbers)

for i in numbers:
    error = 0
    if  i > 1:
        for j in range(2,i):
            if i % j == 0:
                error += 1
        if error == 0:
            cnt += 1
print(cnt)




    
    