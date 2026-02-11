# 에라토스테네스의 체 (Sieve of Eratosthenes)

### 에라토스테네스의 체 알고리즘이란?

에라토스테네스의 체 알고리즘은 소수(prime number)을 판별하는 알고리즘이다.

> 소수 : 1과 자기 자신을 약수로 가지는 수

자연수 N에 대해 에라토스테네스의 체 알고리즘을 수행하면 O(1)의 시간만에 소수 판별이 가능하다.

### 약수의 성질

어떤 자연수 N이 있을 때, N의 약수 A, B에 대해서 $N = A \times B$ 형태로 나타낼 수 있다.

```
ex) n = 8일 때, 약수는 [1, 2, 4, 8] 이므로
n(8) = 1 x 8 또는
n(8) = 2 x 4 으로 표현 가능
```

그렇다면, $N = A \times B$ 에서 $min(A, B)$가 최대가 되는 상황은 언제일까?

```
ex) n = 16 일 때, 약수는 [1, 2, 4, 8 ,16]

n(16) = 1 x 16 : min(A, B) = 1

n(16) = 2 x 8 : min(A, B) = 2

n(16) = 4 x 4 : min(A, B) = 4

이므로, min(A, B) 의 최댓값은 4임.
```

즉, $min(A, B)$가 최대가 되려면 $A = B = \sqrt N$인 상황이 될 것이다.

따라서 A 또는 B 둘 중 하나는 무조건 $\sqrt N$ 이하이기 때문에 1 부터 $\sqrt N$ 이하인 자연수에 대해서만 살펴보면 $N = A \times B$인 모든 경우를 살펴볼 수 있다.

### 에라토스테네스의 체 동작 방식

1 ~ N 까지의 소수를 판별한다고 할 때, 다음과 같은 과정으로 동작한다.

- `is_prime[0 ~ N+1]` 까지 **True**로 초기화
- 1은 소수가 아니므로 **False** 처리
- 2 ~ $\sqrt N$ 반복
  - `is_prime[i]`가 소수면 **True**
  - $i$의 배수들을 모두 **False**로 바꿈 (이때 시작 값은 $i$의 제곱)

### 에라토스테네스의 체 알고리즘

자연수 $N$까지 소수를 판별한다고 하였을 때, 자연수 $i$에 대해 다음과 같이 동작한다. $(2 <= i <= \sqrt N)$

![Image](https://github.com/user-attachments/assets/f0af6d45-0ba0-41df-920f-85ade07b4f72)

### 에라토스테네스의 체 구현 (Python)

```python
import math

def eratosthenes():
    N = 10000
    is_prime = [True] * (N+1)
    is_prime[1] = False

    for i in range(2, int(math.sqrt(N))+1):
        if not is_prime:
            continue

        for j in range(i*i, N+1, i):
            is_prime[j] = False

    primes = set(i for i in range(2, N+1) if is_prime[i])

    return primes
```

시간 복잡도는 $O(N log(logN))$으로 선형 시간에 가깝다.
