num = int(input())

if num % 4 == 0:
    if not num % 100 == 0:
        print("1")
    elif num % 400 == 0:
        print("1")
    else:
        print("0") 
else:
    print("0")