import sys


def main():
    data = sys.stdin.readline().strip()
    n = int(data)
    a = list(range(1, n + 1))
    for i in range(2, n):
        a[i], a[i // 2] = a[i // 2], a[i]
    sys.stdout.write(" ".join(map(str, a)) + "\n")
if __name__ == "__main__":
    main()