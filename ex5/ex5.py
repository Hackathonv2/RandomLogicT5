import sys
from typing import List

def get_max(
    arr: List[int],
    tot: int,
    current: int = 0
) -> int:
    res = tot
    for n in arr:
        if current + n >= tot / 2:
            res = min(res, current + n)
            continue
        tmp = arr.copy()
        tmp.remove(n)
        res = min(res, get_max(tmp, tot, current + n))
    return res

def main():
    lines = [int(line.strip()) for line in sys.stdin.readlines()]
    sys.stdin.close()
    if len(lines) < 3:
        return
    nb_effectif = lines[0]
    arr = lines[2:]
    print(get_max(arr, sum(arr) + nb_effectif, nb_effectif) - nb_effectif)

if __name__ == "__main__":
    main()
