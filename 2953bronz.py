max_num = 0
max_score = 0
for i in range(5):
    a,b,c,d = map(int,input().split())
    
    num = a+ b+ c+ d
    if max_score <  num:
        max_score = num
        max_num = i+1
    

print(max_num, max_score)