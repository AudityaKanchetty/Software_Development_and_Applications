"""Q2: Gradebook (Dictionaries and Sets)"""

grades = {
    "math": {"anna": 1.7, "ben": 2.3, "clara": 1.0},
    "physics": {"ben": 3.0, "clara": 1.3, "david": 2.0},
    "art": {"anna": 1.0, "david": 1.7},
}


def subjects_of(student: str, grades: dict = grades) -> set:
    return {subject for subject, students in grades.items() if student in students}


def takes_all(grades: dict) -> set:
    if not grades:
        return set()
    # Pure set intersection across all subjects
    subject_sets = [set(students.keys()) for students in grades.values()]
    return set.intersection(*subject_sets)


def student_average(grades: dict, student: str) -> float:
    student_grades = [students[student] for students in grades.values() if student in students]
    if not student_grades:
        return 0.0
    return round(sum(student_grades) / len(student_grades), 2)


def honor_roll(grades: dict, limit: float = 1.5) -> list:
    all_students = set()
    for students in grades.values():
        all_students.update(students.keys())
    return sorted(s for s in all_students if student_average(grades, s) <= limit)


# ============================================================================
# DEMO BLOCK
# ============================================================================
if __name__ == "__main__":
    for name in ["anna", "ben", "clara", "david"]:
        print(f"{name} subjects:", subjects_of(name))
        print(f"{name} average:", student_average(grades, name))
    
    print("takes all:", takes_all(grades))
    print("unknown average:", student_average(grades, "zoe"))
    print("honor roll:", honor_roll(grades))