from common import load_input
input = load_input()

def get_direction(first, second):
    return 1 if second - first > 0 else -1

def validate_report(levels):
    dir = get_direction(levels[0], levels[1])
    for i in range(0, len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        adiff = abs(diff)
        if adiff > 3 or adiff < 1 or get_direction(levels[i], levels[i + 1]) != dir:
            return False
    return True

score = 0
reports = input.split("\n")
for report in reports:
    levels = list(map(lambda x: int(x), report.split(" ")))
    if validate_report(levels):
        score += 1
    else:
        for i in range(0, len(levels)):
            copy = levels.copy()
            copy.pop(i)
            if validate_report(copy):
                score += 1
                break

print(score)
