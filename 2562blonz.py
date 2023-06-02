num_list =[]

for i in range(9):
    i = int(input())
    num_list.append(i)

max(num_list)
k = num_list.index(max(num_list))

print(max(num_list))
print(k + 1)
