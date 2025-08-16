import math

def solution(numer1, denom1, numer2, denom2):
    a = (numer1 * denom2) + (numer2 * denom1)  # 분자
    b = denom1 * denom2  # 분모
    c = math.gcd(a, b)  # 최대공약수
    answer = [a // c, b // c] # 기약분수

    return answer