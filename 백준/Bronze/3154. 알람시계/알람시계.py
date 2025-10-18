import sys

arr = [
    [3, 1], [0, 0], [0, 1], [0, 2], [1, 0], 
    [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]
]

def calc(a, b):
    return abs(arr[a][0] - arr[b][0]) + abs(arr[a][1] - arr[b][1])

def main():
    input = sys.stdin.read().strip()
    H, M = map(int, input.split(":"))

    min_distance = float('inf')
    h_result, m_result = 0, 0

    for i in range(100):
        for j in range(100):
            if i % 24 != H or j % 60 != M:
                continue
            
            e = (
                calc(i // 10, i % 10) +
                calc(i % 10, j // 10) +
                calc(j // 10, j % 10)
            )

            if min_distance > e:
                min_distance = e
                h_result, m_result = i, j

    print(f"{h_result:02}:{m_result:02}")

if __name__ == "__main__":
    main()
