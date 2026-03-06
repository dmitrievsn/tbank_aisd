import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    right = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    ans = 0
    for i in range(n):
        l = left[i] + 1
        r = right[i] - 1
        s = pref[r + 1] - pref[l]
        val = s * a[i]
        if val > ans:
            ans = val

    print(ans)


if __name__ == "__main__":
    main()