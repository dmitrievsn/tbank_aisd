import sys

def f(x):
    return x**2 + (x+1)**0.5
C = float(sys.stdin.read().strip())
left = 0
right = C
while right - left > 1e-7:
    mid = (left + right) / 2
    if f(mid) > C:
        right = mid
    elif f(mid) < C:
        left = mid
print(left)