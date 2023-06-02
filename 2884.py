
a,b = map(int,input().split())
c = b + 15

if b> 44 :
    print(a,b-45)
elif a == 0 and b <= 44:
    a = 23 
    print(a, c)
else:
    a-=1

    print(a,c)