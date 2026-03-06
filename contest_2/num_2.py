import sys
from collections import deque


def main():
    data = sys.stdin.read().strip().split()
    n,k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))
    deq = deque()
    for i in range(0,n):
        if not deq:
            deq.append(i)
        else:
            while deq and arr[i] < arr[deq[-1]]:
                deq.pop()
            deq.append(i)
        while deq[0] <= i-k:
            deq.popleft()
        if i >= k-1:
            print(arr[deq[0]])

if __name__ == "__main__":
    main()