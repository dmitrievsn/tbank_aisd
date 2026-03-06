import sys


def main():
    data = sys.stdin.read().strip().split()
    stack = []
    for token in data:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else:
            stack.append(int(token))
    if stack:
        sys.stdout.write(str(stack[-1]))

if __name__ == "__main__":
    main()
