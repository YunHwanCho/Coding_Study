name, num = map(int,input().split())
name_list = {}
for i in range(1,name+1):
    monster = input().rstrip()
    name_list[i] = monster
    name_list[monster] = i
    
for i in range(num):
    hint = input().rstrip()
    if hint.isdigit():  
        print(name_list[int(hint)])

    else:
        print(name_list[hint])
    



