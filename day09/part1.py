# This solution is wildly slow and could be significantly more optimized. I
# ended up going for a solution that mirrored the AoC displayed walkthrough.
# There is certainly a more math based solution here that I did not feel like
# figuring out.

from common import load_input
input = load_input()

def decode(encoded: str):
    res = []
    id = 0
    block = True
    for c in encoded:
        c = int(c)

        if block:
            for _ in range(0, c):
                res.append(str(id))
        else:
            res += '.' * c

        block = not block
        if block:
            id += 1
    return res

def free_block(s: list[str]):
    return '.' in "".join(s) and len(set(s)) == 1

def find_last_taken(ls: list[str]):
    for i, c in enumerate(ls[::-1]):
        if c != '.':
            return (len(ls) - i) - 1
    return -1

def compress_fs(fs: list[str]):
    next_free = fs.index('.')
    while not free_block(fs[next_free:]):
        last_taken_idx = find_last_taken(fs)
        last_taken = fs[last_taken_idx]
        fs[next_free] = last_taken
        fs[last_taken_idx] = '.'
        next_free = fs.index('.')
    return fs

def checksum(fs: list[str]):
    cs = 0
    for i, b in enumerate(fs):
        if b != '.':
            cs += (int(b) * i)
    return cs

fs = decode(input)
fs = compress_fs(fs)
print(checksum(fs))
