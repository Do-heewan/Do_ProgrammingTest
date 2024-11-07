import math

a, b = map(int, input().split())

def bino_coef_factorial(n, k):
	return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

print(bino_coef_factorial(a, b))