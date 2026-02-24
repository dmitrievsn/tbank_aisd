import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return 0, arr
    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]
    left_inv, left_sort = merge_sort(left_part)
    right_inv, right_sort = merge_sort(right_part)
    merge_inv, merged = merge(left_sort, right_sort)
    total_inv = left_inv + right_inv + merge_inv
    return total_inv, merged

def merge(left_part, right_part):
    res = []
    i = j = 0
    inv = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            res.append(left_part[i])
            i += 1
        else:
            res.append(right_part[j])
            inv += len(left_part) - i
            j += 1
    while i < len(left_part):
        res.append(left_part[i])
        i += 1

    while j < len(right_part):
        res.append(right_part[j])
        j += 1

    return inv, res


def main():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))

    inv, sort_arr = merge_sort(arr)
    print(inv)
    print(*sort_arr)


if __name__ == "__main__":
    main()