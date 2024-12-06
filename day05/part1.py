from common import load_input
input = load_input()

[rules, updates] = input.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")

ruleset = {}

for rule in rules:
    [before, after] = rule.split("|")
    if after not in ruleset:
        ruleset[after] = set()
    ruleset[after].add(before)

score = 0
for update in updates:
    nums = [int(x) for x in update.split(",")]
    valid = True
    for i, num in enumerate(nums):
        if not str(num) in ruleset:
            continue
        nextSet = set([str(n) for n in nums[i+1:]])
        if len(nextSet.intersection(ruleset[str(num)])) > 0:
            valid = False
            break
    if valid:
        score += nums[int(len(nums) / 2)]

print(score)
