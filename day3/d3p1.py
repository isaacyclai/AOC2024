import re

with open("input.txt", "r") as f:
    line = f.read()

mul = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
mul = list(map(lambda x:x[4:-1].split(','), mul))
mul = [int(x)*int(y) for x,y in mul]
print(sum(mul))