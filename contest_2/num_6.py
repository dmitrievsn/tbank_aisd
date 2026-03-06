import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = [0] * 100001
    who = [0] * (n + 1)
    front = 0
    back = 0
    ans = []
    i = 1
    for _ in range(n):
        t = data[i]
        if t == 1:
            person_id = data[i + 1]
            pos[person_id] = back
            who[back] = person_id
            back += 1
            i += 2
        elif t == 2:
            front += 1
            i += 1
        elif t == 3:
            back -= 1
            i += 1
        elif t == 4:
            q = data[i + 1]
            ans.append(str(pos[q] - front))
            i += 2
        else:
            ans.append(str(who[front]))
            i += 1
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()