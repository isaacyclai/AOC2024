def check(l):
    prev = 0
    for i in range(1,len(l)):
        cur = l[i] - l[i-1]
        if cur*prev < 0 or abs(cur) < 1 or abs(cur) > 3:
            return i
        prev = cur
    return -1

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [list(map(int, y.split())) for y in lines]

safe = 0
for line in lines:
    i = check(line)
    if i < 0:
        safe += 1
        continue
    for j in range(len(line)):
        l1 = line.copy()
        l1.pop(j)
        if check(l1) < 0:
            safe += 1
            break

print(safe)
