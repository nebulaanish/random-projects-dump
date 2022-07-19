student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for key in student_scores:
    temp = student_scores[key]
    if temp > 90:
        student_grades[key] = "Excellent"
    elif temp > 80:
        student_grades[key] = "Exceeds Expectations"
    elif temp > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = "Fail"
print(student_grades)
