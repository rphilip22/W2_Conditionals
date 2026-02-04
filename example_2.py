#this program assigns a letter grade based on a numeric score
score = int(input("Enter the numeric score (0-100): "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 0:
    grade = 'F'
else:
    grade = 'Invalid score'