import sys


def binary_search(arr, number, length):
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if number == arr[mid]:
            return arr[mid]
        elif number < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if right < 0:
        return arr[0]
    if left >= length:
        return arr[-1]
    diff_left = abs(arr[left] - number)
    diff_right = abs(arr[right] - number)
    if diff_left < diff_right:
        return arr[left]
    elif diff_right < diff_left:
        return arr[right]
    else:
        return min(arr[left], arr[right])


def main():
    data = sys.stdin.read().strip().split()
    n, k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))
    queries = list(map(int, data[2 + n:2 + n + k]))
    results = []

    for query in queries:
        results.append(binary_search(arr, query, n))

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()