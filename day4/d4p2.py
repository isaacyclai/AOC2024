import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def check(startend, s):
    return s[0] == startend[0] and s[-1] == startend[-1]

ans = 0

for i in range(1,len(lines)-1):
    for j in range(1,len(lines[0])-1):
        if lines[i][j] == 'A':
            if check("MM", lines[i-1][j-1:j+2]) and check("SS", lines[i+1][j-1:j+2]) or \
                check("MS", lines[i-1][j-1:j+2]) and check("MS", lines[i+1][j-1:j+2]) or \
                check("SM", lines[i-1][j-1:j+2]) and check("SM", lines[i+1][j-1:j+2]) or \
                check("SS", lines[i-1][j-1:j+2]) and check("MM", lines[i+1][j-1:j+2]):
                ans += 1

print(ans)        
