from common import load_input
input = load_input()
lines = input.split("\n")

left = []
right = []
for line in lines:
    [l, r] = list(map(lambda x: int(x), line.split("   ")))
    left.append(l)
    right.append(r)
left.sort()
right.sort()

score = 0
for (l, r) in zip(left, right):
    score += abs(l - r)
print(score)
