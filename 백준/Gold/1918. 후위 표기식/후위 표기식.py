# 1918 후위표기식

import sys
input = sys.stdin.readline

exp = input()

stack = [] # 연산자들을 담을 스택
result = ''  # 결과 출력

for wrd in exp:
    if (wrd.isalpha()): # 알파벳은 그대로 저장
        result += wrd

    else: # 연산자들에 대해
        if (wrd == "("): # 여는 괄호를 만날시, 스택에 저장
            stack.append(wrd)

        elif (wrd == "*") or (wrd == "/"): # 곱하기 또는 나누기를 만날  경우, 
            while stack and (stack[-1] == "*" or stack[-1] == "/"): # 스택에 연산자가 들어 있고, 스택 제일 위에 곱 또는 나누기일 때 까지
                result += stack.pop() # 결과에 바로 붙여준다.

            stack.append(wrd) # 스택에 연산자 저장

        elif (wrd == "+") or (wrd == "-"): # 더하기 또는 나누기일 경우,
            while stack and (stack[-1] != "("): # 스택에 연산자가 들어 있고, 스택 제일 위에 여는 괄호가 아닐 때 까지
                result += stack.pop() # 결과에 저장
            
            stack.append(wrd) # 스택에 연산자 저장

        elif (wrd == ")"): # 닫는 괄호를 만날 경우
            while stack and (stack[-1] != "("): # 스택에 연산자가 들어 있고, 스택 제일 위에 여는 괄호가 아닐 때 까지
                result += stack.pop() # 결과에 저장

            stack.pop() # 여는 괄호 팝

while stack: # 스택 내부가 빌 때 까지
    result += stack.pop() # 결과에 저장

print(result) # 결과 출력