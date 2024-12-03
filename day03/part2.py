import re
from common import load_input
input = load_input()

to_process = []
start = 0
while True:
    idx = input.find('don\'t()', start)
    if idx == -1:
        to_process.append(input)
        break
    to_process.append(input[start:idx])
    start = idx
    idx = input.find('do()', start)
    if idx == -1:
        break
    input = input[idx:]
    start = 0

regex = r'mul\((\d+),(\d+)\)'
score = 0
for process in to_process:
    groups = re.finditer(regex, process)
    res = [[int(x.group(1)), int(x.group(2))] for x in groups]
    for [x, y] in res:
        score += x * y
print(score)
