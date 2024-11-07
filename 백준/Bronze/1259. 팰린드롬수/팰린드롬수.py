def felind(n):
    count = 0

    if (len(n) % 2 == 0):
        for i in range(len(n) // 2):
            if(n[i] == n[len(n) - 1 - i]):
                count += 1
        if (count == len(n) // 2 ):
            return "yes"
        else:
            return "no"
    if (len(n) % 2 == 1):
        for i in range(len(n) // 2 + 1):
            if(n[i] == n[len(n) - 1 - i]):
                count += 1
        if (count == len(n) // 2 + 1):
            return "yes"
        else:
            return "no"

while(True):
    case = int(input())
    num_len = str(case)

    if(case == 0):
        break
    print(felind(num_len))