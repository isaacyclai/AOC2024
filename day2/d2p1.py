with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [list(map(int, y.split())) for y in lines]
unsafe = 0
for line in lines:
    prev = 0
    for i in range(1,len(line)):
        cur = line[i] - line[i-1]
        if cur*prev < 0 or abs(cur) < 1 or abs(cur) > 3:
            unsafe += 1
            break
        # print(line)
        prev = cur

print(len(lines) - unsafe)
