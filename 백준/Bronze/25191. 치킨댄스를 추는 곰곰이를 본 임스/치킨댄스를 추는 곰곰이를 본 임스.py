chicken = int(input())
coke, beer = map(int, input().split())

if chicken >= coke//2 + beer:
    print(coke//2+beer)
else:
    print(chicken)