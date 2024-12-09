from common import load_input
input = load_input()

def decode(encoded: str):
    res = []
    lists = [], []
    for i, e in enumerate(encoded):
        lists[i%2].append(int(e))
    if len(lists[0]) != len(lists[1]):
        lists[1].append(0)
    for i, (taken, free) in enumerate(list(zip(lists[0], lists[1]))):
        res.append((str(i), taken))
        res.append(('.', free))
    return res


def free_block(s: list[str]):
    return '.' in "".join(s) and len(set(s)) == 1

def find_free_less_than(ls: list[tuple[str, int]], size: int):
    for i, t in enumerate(ls):
        if t[0] == '.' and t[1] >= size:
            return i
    return -1

def find_last_block(ls: list[tuple[str, int]], before: int = 0):
    for i in range(before - 1, -1, -1):
        t = ls[i]
        if t[0].isdigit():
            return i
    return -1

def compress_fs(fs: list[tuple[str, int]]):
    moved = set()
    last_block_idx = find_last_block(fs, len(fs))
    while last_block_idx > - 1:
        last_block = fs[last_block_idx]
        if last_block[0] in moved:
            last_block_idx = find_last_block(fs, last_block_idx)
            continue

        free_block_idx = find_free_less_than(fs, last_block[1])
        if free_block_idx > last_block_idx:
            last_block_idx = find_last_block(fs, last_block_idx)
            continue

        if free_block_idx == -1:
            last_block_idx = find_last_block(fs, last_block_idx)
            continue

        diff = fs[free_block_idx][1] - last_block[1]
        new_free = ('.', last_block[1])
        fs[free_block_idx] = last_block
        fs[last_block_idx] = new_free
        if diff > 0:
            fs.insert(free_block_idx + 1, ('.', diff))
        moved.add(last_block[0])
        last_block_idx = find_last_block(fs, last_block_idx)
    return fs

def string_fs(fs: list[tuple[str, int]]):
    res = ""
    for b in fs:
        res += (b[0] * b[1])
    return res

def checksum(fs: list[tuple[str, int]]):
    cs = 0
    idx = 0
    for block in fs:
        if block[0] == '.':
            idx += block[1]
        else:
            for _ in range(0, block[1]):
                cs += (idx * int(block[0]))
                idx += 1
    return cs

fs = decode(input)
fs = compress_fs(fs)
cs = checksum(fs)
print(cs)
