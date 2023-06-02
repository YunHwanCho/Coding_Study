num = int(input())
n = num

first = num//10
second = num%10
third = (first + second) % 10
four = (second*10) + third
k = 0
while  True:
    first = num//10
    second = num%10
    third = (first + second) % 10
    num = (second*10) + third
    k += 1
    if n == num: 
        break

print(k)

     