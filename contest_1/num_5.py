import sys

data = sys.stdin.read().strip().split()
a, b, c, d = map(int, data)
def f(x):
    return a*x**3 + b*x**2 + c*x + d
left = -10**6
right = 10**6
while f(left) * f(right) > 0:
    left *= 2
    right *= 2
if a > 0:
    while right - left > 1e-7:
        mid = (left + right) / 2
        if f(mid) > 0:
            right = mid
        else:
            left = mid
else:
    while right - left > 1e-7:
        mid = (left + right) / 2
        if f(mid) > 0:
            left = mid
        else:
            right = mid

print("{:.10f}".format(left))