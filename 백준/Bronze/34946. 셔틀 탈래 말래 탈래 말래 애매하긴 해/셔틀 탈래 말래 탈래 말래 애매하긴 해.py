# 34946 셔틀 탈래 말래 탈래 말래 애매하긴 해

A, B, C, D = map(int, input().split())

shuttle = A+B
walk = C

lect = D

if shuttle <= lect and walk <= lect:
  print("~.~")
elif shuttle <= lect:
  print("Shuttle")
elif walk <= lect:
  print("Walk")
else:
  print("T.T")