class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = []

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: Оценивать можно только Лекторов'
        if course not in self.courses_in_progress:
            return 'Ошибка: Студент не изучает этот курс'
        if course not in lecturer.courses_attached:
            return 'Ошибка: Лектор не закреплён за этим курсом'
        lecturer.grades.append(grade)
        
        
        
        
        
class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = []

class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}  



        
