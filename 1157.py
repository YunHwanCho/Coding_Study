str = input()
low = str.lower()
n_list = list(low)
num = []
for i in range(ord('a'), ord('z')+1):
    num.append(n_list.count(chr(i)))

k = max(num)

for _ in range(ord(97),ord(123)):
    