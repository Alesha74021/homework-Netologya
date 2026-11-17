class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Reviewer( {self.name}, {self.surname} )'

    
class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.average_grades = {}
    def __str__(self):
        return f'Lecturer( {self.name}, {self.surname} )'
        
    
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.completed_courses = []
        self.grades = {}
        self.average_grades = {}

    def __str__(self):
        return f'Student( {self.name}, {self.surname} )'

some_reviewer = Reviewer('Some','Buddy')
print(some_reviewer)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.average_grades['lectures'] = [9.9]
print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 'you_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.completed_courses += ['Введение в программирование']
some_student.average_grades['homework'] = [9.9]
some_student.courses_in_progress += ['Python', 'Git']
some_student.completed_courses += ['Введение в прогаммирование']
print(some_student)



    
        
        
        