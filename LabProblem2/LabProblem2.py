#Weights
zbW = 10
attendanceW = 5
labW = 42
quizW = 10
midtermW = 13
finalW = 20
totalW = 100

#Grades
zbG = float(input("What is your grade for zyBooks: "))
print(f"You have a {zbG}% for zyBooks, which is {zbW}% of your final grade.")
attendanceG = float(input("What is your grade for attendance: "))
print(f"You have a {attendanceG}% for attendance, which is {attendanceW}% of your final grade.")
labG = float(input("What is your grade for lab: "))
print(f"You have a {labG}% for lab, which is {labW}% of your final grade.")
quizG = float(input("What is your grade for quizzes: "))
print(f"You have a {quizG}% for quizzes, which is {quizW}% of your final grade.")
midtermG = float(input("What is your grade for midterm: "))
print(f"You have a {midtermG}% for midterm, which is {midtermW}% of your final grade.")

curWeightSum = zbW + attendanceW + labW + quizW + midtermW
curWeightedGradeSum = (zbG * zbW) + (attendanceG * attendanceW) + (labG * labW) + (quizG * quizW) + (midtermG * midtermW)

avgGrade = (curWeightedGradeSum) /curWeightSum

print(f"You have a {avgGrade: .2f}% so far")

excludedWeight = finalW
desiredGrade = float(input("What is your desired grade for the class "))

neededPercent =((desiredGrade * 100) - curWeightedGradeSum) / excludedWeight
print(f"To get a {desiredGrade}% for this class you need a {neededPercent: .2f}% for your final exam")

