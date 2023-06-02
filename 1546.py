
num = int(input())

numbers = list(map(int, input().split()))

M = max(numbers)



new_numbers = []
for score in numbers:
    new_numbers.append(score/M * 100)
    
real_middle = sum(new_numbers)/num
 

print(real_middle)


    




    