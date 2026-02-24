import sys
n = int(input())
def query(x):
    print(x)
    sys.stdout.flush()
    return input()
left= 1
right= n
while left <= right:
    mid = (right+left)//2
    ans = query(mid)
    if ans == '<':
        right = mid - 1
    else:
        left = mid
print(f"! {left}")
sys.stdout.flush()
