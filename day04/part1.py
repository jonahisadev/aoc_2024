from common import load_input
input = load_input()

def grid_range(grid, x1, y1, x2, y2):
    h = len(grid)
    w = len(grid[0])
    if x2 < -1 or x2 > w or y2 < -1 or y2 > h:
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

    return res


def create_strings(grid, x, y):
    all_options = [
        grid_range(grid, x, y, x + 4, y),
        grid_range(grid, x, y, x - 4, y),
        grid_range(grid, x, y, x, y + 4),
        grid_range(grid, x, y, x, y - 4),
        grid_range(grid, x, y, x + 4, y + 4),
        grid_range(grid, x, y, x + 4, y - 4),
        grid_range(grid, x, y, x - 4, y + 4),
        grid_range(grid, x, y, x - 4, y - 4),
    ]

    return list(map(lambda x: "".join(x), all_options))

def find_xmas(grid, x, y):
    c = grid[y][x]
    if c != 'X':
        return 0
    strs = create_strings(grid, x, y)
    return strs.count("XMAS")

lines = input.split("\n")
grid = []
for line in lines:
    grid.append(list(line))

score = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        score += find_xmas(grid, x, y)
print(score)
