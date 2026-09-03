#Weights
zbW = 10
attendanceW = 5
labW = 42
quizW = 10
midtermW = 13
finalW = 20
totalW = 100

#Grades
zbG = 97.3
attendanceG = 100.00
labG = 89.72
quizG = 86.24
midtermG = 87.5
finalG = 0.00

curWeightSum = zbW + attendanceW + labW + quizW + midtermW
curWeightedGradeSum = (zbG * zbW) + (attendanceG * attendanceW) + (labG * labW) + (quizG * quizW) + (midtermG * midtermW)

avgGrade = (curWeightedGradeSum) /curWeightSum

print(f"{avgGrade: .2f}")

excludedWeight = finalW
desiredGrade = 90

neededPercent =((desiredGrade * 100) - curWeightedGradeSum) / excludedWeight
print(f"{neededPercent: .2f}")
