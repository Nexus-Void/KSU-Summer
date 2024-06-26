# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: assignment 4
def average_grade(name, grade1=-1.0, grade2=-1.0, grade3=-1.0, grade4=-1.0, grade5=-1.0, grade6=-1.0, grade7=-1.0,
                  grade8=-1.0, grade9=-1.0, grade10=-1.0, grade11=-1.0, grade12=-1.0):
    if name == "Labs":
        return (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10 + grade11
                + grade12) / 12
    if name == "Assignments":
        return (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7) / 7
    if name == "Midterm":
        return grade1 / 1
    if name == "Exam":
        return grade1 / 1


def weighted_average(average, weight):
    return round(average * weight, 3)


print("[CSE 1321L Grade Calculator]")

print("Labs")
weight1 = 0.10
g1 = float(input("Enter Grade #1: "))
g2 = float(input("Enter Grade #2: "))
g3 = float(input("Enter Grade #3: "))
g4 = float(input("Enter Grade #4: "))
g5 = float(input("Enter Grade #5: "))
g6 = float(input("Enter Grade #6: "))
g7 = float(input("Enter Grade #7: "))
g8 = float(input("Enter Grade #8: "))
g9 = float(input("Enter Grade #9: "))
g10 = float(input("Enter Grade #10: "))
g11 = float(input("Enter Grade #11: "))
g12 = float(input("Enter Grade #12: "))
labs_average = average_grade("Labs", g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12)
lwa = weighted_average(labs_average, weight1)
print("Weighted Points:", lwa, "\n")

print("Assignments")
weight2 = 0.40
g1 = float(input("Enter Grade #1: "))
g2 = float(input("Enter Grade #2: "))
g3 = float(input("Enter Grade #3: "))
g4 = float(input("Enter Grade #4: "))
g5 = float(input("Enter Grade #5: "))
g6 = float(input("Enter Grade #6: "))
g7 = float(input("Enter Grade #7: "))
assignment_average = average_grade("Assignments", g1, g2, g3, g4, g5, g6, g7)
awa = weighted_average(assignment_average, weight2)
print("Weighted Points:", awa, "\n")

print("Midterm")
weight3 = 0.20
g1 = float(input("Enter Grade #1: "))
midterm_average = average_grade("Midterm", g1)
mwa = weighted_average(midterm_average, weight3)
print("Weighted Points:", mwa, "\n")

print("Exam")
weight4 = 0.30
g1 = float(input("Enter Grade #1: "))
exam_average = average_grade("Exam", g1)
ewa = weighted_average(exam_average, weight4)
print("weighted Points:", ewa, "\n")

final_grade = lwa + awa + mwa + ewa
print("Your final grade for CSE1321L is:", final_grade)
