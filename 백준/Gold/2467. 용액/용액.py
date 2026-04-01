# 2467 용액

def binary_search(arr, start, end):
    min_value = float('inf')
    result = []

    while start < end:
        curr = arr[start] + arr[end]

        if abs(curr) < min_value:
            min_value = abs(curr)
            result = [arr[start], arr[end]]

        if curr < 0:
            start += 1
        else:
            end -= 1

    return result

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(*binary_search(lst, 0, N-1))