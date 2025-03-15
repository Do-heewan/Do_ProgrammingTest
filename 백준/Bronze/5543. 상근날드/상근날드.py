bug1 = int(input())
bug2 = int(input())
bug3 = int(input())
drink1 = int(input())
drink2 = int(input())

bugger = [bug1, bug2, bug3]
drink = [drink1, drink2]

bugger.sort()
drink.sort()

print(bugger[0] + drink[0] - 50)