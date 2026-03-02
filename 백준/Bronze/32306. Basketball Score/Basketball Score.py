# 32306 Basketball Score

team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

score1 = 0
score2 = 0
for i in range(3):
  score1 += team1[i] * (i+1)
  score2 += team2[i] * (i+1)

if score1 > score2:
  print(1)
elif score1 < score2:
  print(2)
else:
  print(0)