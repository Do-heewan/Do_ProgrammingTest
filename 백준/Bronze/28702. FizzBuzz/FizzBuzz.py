case = []

# case 리스트 만들기
for i in range(3):
    word = input()
    
    if (word == "FizzBuzz"):
        case.append("fb")
    elif (word == "Fizz"):
        case.append("f")
    elif (word == "Buzz"):
        case.append("b")
    else:
        num = int(word)
        case.append("n")

for i in range(len(case)):
    if(case[i] == "n"):
        pos = 3 - i

for i in range (1, 16):
    if (i == num % 15):
        result_pos = i + pos
        result = result_pos + (num // 15) * 15

def final(n):
    if (n % 3 == 0) & (n % 5 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0) & (n % 5 != 0):
        print("Fizz")
    elif (n % 5 == 0) & (n % 3 != 0):
        print("Buzz")
    else:
        print(n)
        
final(result)