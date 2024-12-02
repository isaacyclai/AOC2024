with open("input.txt", "r") as f:
    lines = f.readlines()

l1, l2 = [], []
for row in lines:
    a, b = row.split()
    l1.append(int(a))
    l2.append(int(b))
l1.sort()
l2.sort()
ans = 0
for i in range(len(l1)):
    ans += abs(l1[i]-l2[i])
print(ans)