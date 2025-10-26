N = int(input())
major = input()
d = {"B" : 0, "S" : 0, "A" : 0}
for m in major:
    d[m] += 1

res = ''
for k, v in d.items():
    if v == max(d.values()):
        res += k

print(res) if res != "BSA" else print("SCU")