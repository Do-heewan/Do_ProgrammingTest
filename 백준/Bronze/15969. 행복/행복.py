N = int(input())
student = list(map(int, input().split()))
print(max(student) - min(student))