hour, minute = map(int,input().split())
time = int(input())

a = (minute + time) // 60
b = (minute + time) % 60

if (minute + time)>= 60:
    if hour + a >= 24:
        hour = hour - 24
    hour = hour + a
    print(hour, b)

else:
    minute = minute + time
    print(hour, minute)