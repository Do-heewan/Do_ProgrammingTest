# 스택(Stacks)

### 스택(Stacks)이란?

스택은 자료를 보관하는 선형 구조 중 하나로, 한 방향으로 넣고(Push) 같은 방향으로 뽑는(Pop) 방식으로 동작한다.

즉 입구와 출구가 같기 때문에 **후입선출(LIFO, Last In First Out)** 의 특징을 갖는다.

<br>

### 스택의 동작 예시

![스택](https://github.com/user-attachments/assets/7b79fa1b-196b-4638-a21b-3a7b439f05a7)

<br>

### 스택의 구현

파이썬에서 스택은 리스트를 이용하여 구현할 수 있다.

``` python
stack = []

stack.append(1) # push = append
stack.append(2)
stack.append(3)

stack.pop() # pop을 하면 가장 마지막에 push된 3이 나온다.
```