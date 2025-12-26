# 5622 다이얼

alph = input()
dial_list = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for a in alph:
    for dial in dial_list:
        if a in dial:
            time += dial_list.index(dial)

    time += 1

print(time)