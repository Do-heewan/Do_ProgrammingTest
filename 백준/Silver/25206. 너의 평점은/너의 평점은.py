# 25206 너의 평점은

sc = {"A+" : 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}

all_score = 0
sum_scgd = 0
scores = 0
for _ in range(20):
    subj, score, grade = input().split()

    if grade == "P":
        continue

    scores += float(score)
    scoreOfGrade = float(score) * sc[grade]
    sum_scgd += scoreOfGrade

all_score = sum_scgd / scores
print(all_score)