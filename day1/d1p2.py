with open("input.txt", "r") as f:
    lines = f.readlines()

l1, l2 = [], []
for row in lines:
    a, b = row.split()
    l1.append(int(a))
    l2.append(int(b))

print(sum(map(lambda x:x*l2.count(x), l1)))
