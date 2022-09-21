import sys
input = sys.stdin.readline

def grade_to_point(grade):
    grade_table = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
    }
    return grade_table[grade]

def calc_gpa(course):
    credits, grade_points = 0, 0
    for subject in course:
        _, credit, grade = subject.split()
        if grade == 'P':
            continue
        credits += float(credit)
        grade_points += grade_to_point(grade) * float(credit)
    return grade_points / credits

course = []
for _ in range(20):
    subject = input()
    course.append(subject)
gpa = calc_gpa(course)
print('%.6f' %gpa)