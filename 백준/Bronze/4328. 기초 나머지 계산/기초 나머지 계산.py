def to_base(n, b):
    if n == 0:
        return "0"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    digits = []
    while n > 0:
        digits.append(str(n % b))
        n //= b

    return sign + "".join(reversed(digits))


while True:
    line = input().strip()
    if line == "0":
        break

    b, p, m = line.split()
    b = int(b)

    p = int(p, b)
    m = int(m, b)

    res = p % m

    print(to_base(res, b))
