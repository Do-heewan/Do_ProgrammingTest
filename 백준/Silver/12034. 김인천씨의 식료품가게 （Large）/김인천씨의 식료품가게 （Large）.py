# 12034 김인천씨의 식료품가게 (Large)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    case = []
    for x in price:
        if int(x * 100 / 75) in price:
            case.append(x)
            price.remove(int(x * 100 / 75))

    print(f"Case #{t}:", *case)