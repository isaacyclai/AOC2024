import re

with open("input.txt", "r") as f:
    line = f.read()

# ? makes the dot lazy, DOTALL searches across newlines
line = re.findall(r"do\(\).+?don't\(\)", f"do(){line}don't()", re.DOTALL) 

def mul_all(s):
    mul = re.findall(r"mul\([0-9]+,[0-9]+\)", s)
    mul = list(map(lambda x:x[4:-1].split(','), mul))
    mul = [int(x)*int(y) for x,y in mul]
    return sum(mul)
print(sum(map(mul_all, line)))