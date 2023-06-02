num = int(input())

word_list = []
for i in range(num):
    word_list.append(input())
no_list = list(set(word_list))

no_list = sorted(no_list, key = lambda x: (len(x), x))

    
for i in no_list:
    print(i)
    










