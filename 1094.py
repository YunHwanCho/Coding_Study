want = int(input())
num = 64
k = 0
list = []
find = False


if num//2 == want or num == want:
    k += 1
    print(k)
    find = True
    
    
while sum(list) != want and not find:
    key = num
    for _ in range(6):
        key /= 2
        if key <= want and sum(list) + key <= want:
            list.append(key)
            k += 1
        if sum(list) == want:
            print(k)
            break
               
                
            