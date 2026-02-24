import sys

def binary_search(arr, number, length):
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if number == arr[mid]:
            return "YES"
        elif number < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return "NO"

def main():
    data = sys.stdin.read().strip().split()
    n, k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))
    queries = list(map(int, data[2 + n:2 + n + k]))
    results = []
    for query in queries:
        results.append(binary_search(arr, query, n))
    print("\n".join(results))


if __name__ == "__main__":
    main()