import sys
from math import isqrt


def solve_one(n: int, m: int):
    N = n * m
    T = N * (N + 1) // 2

    best_diff = None
    best_dir = None
    best_x = None

    if m >= 2:
        A = m * (n - 1) + 1

        B = n * A
        D = B * B + 4 * n * T
        k0 = (isqrt(D) - B) // (2 * n)

        # Проверяем несколько соседей вокруг корня
        lo = max(1, k0 - 3)
        hi = min(m - 1, k0 + 3)

        for k in range(lo, hi + 1):
            s = n * k * (A + k) // 2
            diff = abs(T - 2 * s)
            x = k + 1
            if (best_diff is None
                    or diff < best_diff
                    or (diff == best_diff and best_dir != 'V')  # вертикальный приоритет
                    or (diff == best_diff and best_dir == 'V' and x < best_x)):
                best_diff = diff
                best_dir = 'V'
                best_x = x

    if n >= 2:
        D = 1 + 4 * T
        M0 = (isqrt(D) - 1) // 2
        h0 = M0 // m

        lo = max(1, h0 - 3)
        hi = min(n - 1, h0 + 3)

        local_best_diff = None
        local_best_x = None

        for h in range(lo, hi + 1):
            M = h * m
            s = M * (M + 1) // 2
            diff = abs(T - 2 * s)
            x = h + 1
            if (local_best_diff is None
                    or diff < local_best_diff
                    or (diff == local_best_diff and x < local_best_x)):
                local_best_diff = diff
                local_best_x = x

        if (best_diff is None
                or local_best_diff < best_diff
                or (local_best_diff == best_diff and best_dir != 'V' and local_best_x < best_x)):
            if best_dir == 'V' and local_best_diff == best_diff:
                pass
            else:
                best_diff = local_best_diff
                best_dir = 'H'
                best_x = local_best_x

    return best_dir, best_x


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    ptr = 1

    for _ in range(t):
        n = data[ptr]
        m = data[ptr + 1]
        ptr += 2
        d, x = solve_one(n, m)
        out.append(f"{d} {x}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()