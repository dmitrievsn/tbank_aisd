import sys
from collections import deque


def main():
    input = sys.stdin.readline
    n = int(input())
    left = deque()
    right = deque()
    ans = []

    for _ in range(n):
        s = input().split()

        if s[0] == '+':
            right.append(int(s[1]))
            if len(right) > len(left):
                left.append(right.popleft())
        elif s[0] == '*':
            left.append(int(s[1]))
            if len(left) > len(right) + 1:
                right.appendleft(left.pop())
        else:
            ans.append(str(left.popleft()))
            if len(left) < len(right):
                left.append(right.popleft())

    sys.stdout.write('\n'.join(ans))


if __name__ == "__main__":
    main()