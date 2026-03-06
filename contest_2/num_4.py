import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    colors = []
    counts = []
    for x in a:
        if colors and colors[-1] == x:
            counts[-1] += 1
        else:
            colors.append(x)
            counts.append(1)
    m = len(colors)
    start = -1
    for i in range(m):
        if counts[i] >= 3:
            start = i
            break
    if start == -1:
        print(0)
        return
    destroyed = counts[start]
    left = start - 1
    right = start + 1
    while left >= 0 and right < m and colors[left] == colors[right]:
        if counts[left] + counts[right] >= 3:
            destroyed += counts[left] + counts[right]
            left -= 1
            right += 1
        else:
            break
    print(destroyed)

if __name__ == "__main__":
    main()