import re
from common import load_input
input = load_input()

regex = r'mul\((\d+),(\d+)\)'
groups = re.finditer(regex, input)

res = [[int(x.group(1)), int(x.group(2))] for x in groups]

score = 0
for [x, y] in res:
    score += x * y
print(score)
