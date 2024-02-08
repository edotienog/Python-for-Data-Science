def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(get_grade(60))
print(get_grade(87))
