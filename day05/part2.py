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
    i = 0
    while i < len(nums):
        num = nums[i]
        if not str(num) in ruleset:
            continue
        nextSet = set([str(n) for n in nums[i+1:]])
        violations = nextSet.intersection(ruleset[str(num)])
        if len(violations) > 0:
            valid = False
            foundIndex = nums.index(int(list(violations)[0]))
            temp = nums[foundIndex]
            nums[i] = temp
            nums[foundIndex] = num
            continue
        i += 1
    if valid == False:
        score += nums[int(len(nums) / 2)]

print(score)
