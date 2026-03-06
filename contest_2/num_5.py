import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    arr = [int(x) for x in it]
    if len(arr) > n:
        arr = arr[:n]
    expected = 1
    stack = []
    ops = []
    def push_op(typ: int, k: int) -> None:
        if k <= 0:
            return
        if ops and ops[-1][0] == typ:
            ops[-1] = (typ, ops[-1][1] + k)
        else:
            ops.append((typ, k))
    for x in arr:
        push_op(1, 1)
        stack.append(x)
        while stack and stack[-1] == expected:
            stack.pop()
            push_op(2, 1)
            expected += 1
    while stack and stack[-1] == expected:
        stack.pop()
        push_op(2, 1)
        expected += 1
    if expected - 1 != n:
        sys.stdout.write("0")
        return
    out_lines = [str(len(ops))]
    out_lines += [f"{t} {k}" for (t, k) in ops]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()