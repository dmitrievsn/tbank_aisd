import sys
from array import array


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    p = data[1:1 + n]
    size = 1
    while size < n:
        size <<= 1

    NEG = -10**9
    m = 2 * size

    length = array('I', [0]) * m
    cnt = array('I', [0]) * m
    best = array('i', [NEG]) * m
    for i in range(n):
        v = size + i
        length[v] = 1
        cnt[v] = 1
        best[v] = 0
    for v in range(size - 1, 0, -1):
        l = v << 1
        r = l | 1
        length[v] = length[l] + length[r]
        cnt[v] = cnt[l] + cnt[r]
        cand = (length[l] - cnt[l]) + best[r]
        best[v] = best[l] if best[l] > cand else cand

    ans = ["1"]
    for pos in p:
        v = size + pos - 1
        cnt[v] = 0
        best[v] = NEG
        v >>= 1
        while v:
            l = v << 1
            r = l | 1
            cnt[v] = cnt[l] + cnt[r]
            cand = (length[l] - cnt[l]) + best[r]
            best[v] = best[l] if best[l] > cand else cand
            v >>= 1
        root_best = best[1]
        ans.append(str(1 if root_best < 0 else root_best + 1))

    sys.stdout.write(" ".join(ans) + "\n")


if __name__ == "__main__":
    main()