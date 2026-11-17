def get_average_grade(grades):
    all_grades = []

    for course_grades in grades.values():
        all_grades.extend(course_grades)

    if not all_grades:
        return 0.0

    return round(sum(all_grades) / len(all_grades), 1)


class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def __str__(self):
        average_grade = get_average_grade(self.grades)

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average_grade}"
        )


class Student:
    def __init__(self, name, surname, courses_attached, courses_finished):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached
        self.courses_finished = courses_finished
        self.grades = {}

    def __str__(self):
        average_grade = get_average_grade(self.grades)

        courses_attached = ", ".join(self.courses_attached)
        courses_finished = ", ".join(self.courses_finished)

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade}\n"
            f"Курсы в процессе изучения: {courses_attached}\n"
            f"Завершенные курсы: {courses_finished}"
        )


some_reviewer = Reviewer("Some", "Buddy")

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.grades = {
    "Python": [10, 9.8, 9.9]
}

some_student = Student(
    "Ruoy",
    "Eman",
    ["Python", "Git"],
    ["Введение в программирование"]
)
some_student.grades = {
    "Python": [10, 9.8],
    "Git": [9.9]
}

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)



    
        
        
        