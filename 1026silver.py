num = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)

s = 0

for i in range(num):
    s += sorted_a[i] * sorted_b[i]

print(s)


# j = min(a_list)
# k = max(b_list)      

# print(j)
# print(k)