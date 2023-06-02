num = int(input())
box = []

cnt = 0
for i in range(num):
    word = input()
    box.append(word)
    error = 0

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                error += 1

    if error == 0:
        cnt += 1

print(cnt)
    


   


