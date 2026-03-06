import sys


def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    i = 1
    stack = []
    for _ in range(n):
        op = int(data[i])
        if op == 1:
            if not stack:
                stack.append((int(data[i + 1]),int(data[i + 1])))
                i+=2 
            else:
                stack.append((int(data[i + 1]),min(int(data[i + 1]),stack[-1][1])))
                i += 2
        elif op == 2:
            stack.pop()
            i += 1
        else:
            print(stack[-1][1])
            i += 1

if __name__ == "__main__":
    main()