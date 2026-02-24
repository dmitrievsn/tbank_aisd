import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1].strip()
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('A')] += 1
    left_parts = []
    for i in range(26):
        left_parts.append(chr(ord('A') + i) * (cnt[i] // 2))
    left = "".join(left_parts)
    mid = ""
    for i in range(26):
        if cnt[i] % 2 == 1:
            mid = chr(ord('A') + i)
            break
    ans = left + mid + left[::-1]
    sys.stdout.write(ans + "\n")

if __name__ == "__main__":
    main()