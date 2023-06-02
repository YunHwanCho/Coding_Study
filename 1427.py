num = int(input())

number = list(str(num))





#내림차순 정렬


reversed_number = sorted(number, reverse=True)
result = int(''.join([str(num) for num in reversed_number]))
print(result)

# for num in number:
#     if len(reversed_number) == 0:
#         reversed_number.append(num)
#     else:
#         for i in range(len(reversed_number)):
#             if num > reversed_number[i]:
#                 reversed_number.insert(i, num)
#                 break

#         else:
#             reversed_number.append(i)        



    


