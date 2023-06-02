num = int(input())

num_list = []

for i in range(num):
    a = int(input())
    num_list.append(a)



for i in range(0,num-1):
    least = i
    for j in range(i+1, num):
        if num_list[least] > num_list[j]:
            least = j
    num_list[i], num_list[least] = num_list[least], num_list[i]



for i in range(num):
    print(num_list[i])

