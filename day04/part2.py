import itertools
from common import load_input
input = load_input()

def grid_range(grid, x1, y1, x2, y2):
    h = len(grid)
    w = len(grid[0])

    if x1 < 0 or x1 >= w or x2 < 0 or x2 >= w or y1 < 0 or y1 >= h or y2 < 0 or y2 >= h:
        return []

    res = []
    dx = x2 - x1
    dy = y2 - y1
    stepX = int(dx / max([abs(n) for n in [dx, dy]]))
    stepY = int(dy / max([abs(n) for n in [dx, dy]]))

    while x1 != x2 or y1 != y2:
        res.append(grid[y1][x1])
        x1 += stepX
        y1 += stepY
    res.append(grid[y1][x1])
    x1 += stepX
    y1 += stepY

    return res


def create_strings(grid, x, y):
    all_options = [
        grid_range(grid, x - 1, y - 1, x + 1, y + 1),
        grid_range(grid, x - 1, y + 1, x + 1, y - 1)
    ]
    all_options = list(itertools.chain(*[[s, s[::-1]] for s in all_options]))

    return list(map(lambda x: "".join(x), all_options))

def find_xmas(grid, x, y):
    c = grid[y][x]
    if c != 'A':
        return 0
    strs = create_strings(grid, x, y)
    return strs.count("MAS") == 2

lines = input.split("\n")
grid = []
for line in lines:
    grid.append(list(line))

score = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        score += 1 if find_xmas(grid, x, y) else 0
print(score)
