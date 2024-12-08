import string
from common import load_input
input = load_input()

class Grid:
    def __init__(self, s):
        self.data = [list(y) for y in s.split("\n")]
        self.width = len(self.data[0])
        self.height = len(self.data)

    def at_xy(self, x, y):
        return self.data[y][x]

    def at(self, coord):
        return self.at_xy(coord[0], coord[1])

    def find(self, c, sx = 0, sy = 0):
        skipped = False
        for y in range(sy, self.height):
            sx = 0 if skipped else sx
            for x in range(sx, self.width):
                if self.at_xy(x, y) == c:
                    return (x, y)
            skipped = True
        return (-1, -1)

    def find_exclude(self, c, excl, sx = 0, sy = 0):
        p = self.find(c, sx, sy)
        if p == excl:
            return self.find(c, p[0] + 1, p[1])
        return p

    def validate_coord(self, coord):
        return coord[0] >= 0 and coord[0] < self.width and coord[1] >= 0 and coord[1] < self.height

    def relative(self, start, rel):
        new_coord = (start[0] + rel[0], start[1] + rel[1])
        if not self.validate_coord(new_coord):
            return None
        return self.at(new_coord)

    def dist(self, p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

grid = Grid(input)
antinodes = set()
for c in string.ascii_letters + string.digits:
    last_point = (-1, 0)

    while True:
        curr_point = grid.find(c, last_point[0] + 1, last_point[1])
        if curr_point == (-1, -1):
            break
        next_point = (-1, 0)
        while True:
            next_point = grid.find_exclude(c, curr_point, next_point[0] + 1, next_point[1])
            if next_point == (-1, -1):
                break
            distance = grid.dist(curr_point, next_point)
            an = (next_point[0] + distance[0], next_point[1] + distance[1])
            if grid.validate_coord(an):
                antinodes.add(an)
        last_point = curr_point

print(len(antinodes))
