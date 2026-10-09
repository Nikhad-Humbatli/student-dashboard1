"""Task 2: Clean Code refactoring nümunəsi."""

# ---------- ƏVVƏL (pis kod) ----------
# def f(x, y):
#     if y >= 90: return [x, y, "A"]
#     elif y >= 80: return [x, y, "B"]
#     elif y >= 70: return [x, y, "C"]
#     elif y >= 60: return [x, y, "D"]
#     else: return [x, y, "F"]
# l = [["Ali",85],["Leyla",72],["Murad",48]]
# t = 0
# for i in l: t = t + i[1]
# print(t / len(l))
# for i in l: print(f(i[0], i[1]))

# ---------- SONRA (clean code) ----------
GRADE_A_MIN_SCORE = 90
GRADE_B_MIN_SCORE = 80
GRADE_C_MIN_SCORE = 70
GRADE_D_MIN_SCORE = 60


def calculate_grade(score):
    if score >= GRADE_A_MIN_SCORE:
        return "A"
    if score >= GRADE_B_MIN_SCORE:
        return "B"
    if score >= GRADE_C_MIN_SCORE:
        return "C"
    if score >= GRADE_D_MIN_SCORE:
        return "D"
    return "F"


def calculate_average(scores):
    return sum(scores) / len(scores)


def print_student_results(students):
    for student_name, student_score in students:
        print(student_name, student_score, calculate_grade(student_score))


if __name__ == "__main__":
    students = [("Ali", 85), ("Leyla", 72), ("Murad", 48)]
    print(calculate_average([score for _, score in students]))
    print_student_results(students)
