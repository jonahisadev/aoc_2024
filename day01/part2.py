from common import load_input
input = load_input()
lines = input.split("\n")

left = []
right = []
for line in lines:
    [l, r] = list(map(lambda x: int(x), line.split("   ")))
    left.append(l)
    right.append(r)

score = 0
for l in left:
    score += right.count(l) * l
print(score)
