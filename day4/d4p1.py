import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def find(arr):
    ans = 0
    for row in arr:
        s = ""
        for c in row:
            s += c
        for i in range(len(s)):
            if s[i:i+4] == "XMAS" or s[i:i+4] == "SAMX":
                ans += 1
    return ans

rows = np.empty(shape=(len(lines), len(lines[0])),dtype=str)

for i in range(len(lines)):
    for j in range(len(lines)):
        rows[i][j] = lines[i][j]

n = len(rows)

cols = rows.T

l_diag = []
for i in range(-n+1,n):
    l_diag.append(np.diagonal(rows, i))

r_diag = []
for i in range(-n+1,n):
    r_diag.append(np.diagonal(np.fliplr(rows), i))

print(find(rows)+find(cols)+find(l_diag)+find(r_diag))

        
