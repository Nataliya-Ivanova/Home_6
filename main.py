class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')
            return

    @property
    def rate_average_grade(self):
        all_grades = []
        for course in self.courses_in_progress:
            grades_stud = self.grades.get(course)
            all_grades += grades_stud
        average_grade = sum(all_grades) / len(all_grades)
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректно введен студент')
            return
        else:
            self_av = self.rate_average_grade
            other_av = other.rate_average_grade
            return self_av < other_av

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашку: {self.rate_average_grade:.2f} ' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @property
    def rate_average_grade(self):
        all_grades = []
        for course in self.courses_attached:
            grades_lec = self.grades.get(course)
            all_grades += grades_lec
        average_grade = sum(all_grades) / len(all_grades)
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректно введен лектор')
            return
        else:
            self_av = self.rate_average_grade
            other_av = other.rate_average_grade
            return self_av < other_av

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rate_average_grade:.2f}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached or course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

major_lecturer = Lecturer('Some', 'Buddy')
major_lecturer.courses_attached += ['Python', 'Web', 'Boss']
major_lecturer.grades = {'Python': [1, 5, 7], 'Web': [8, 10], 'Boss': [9, 2, 3, 7]}

print(major_lecturer)

major_lecturer_2 = Lecturer('So', 'Bu')
major_lecturer_2.courses_attached = ['Python', 'Web', 'Boss']
major_lecturer_2.grades = {'Python': [10, 5, 7, 8], 'Web': [10], 'Boss': [9, 2, 3, 7]}
print(major_lecturer_2)

print(major_lecturer > major_lecturer_2)

major_student = Student('Natali', 'Ivanova', 'woman')
major_student.courses_in_progress = ['Python', 'Web', 'Boss']
major_student.finished_courses  = ['С++', 'Design']
major_student.grades = {'Python': [10,5,7], 'Web': [10], 'Boss': [9, 2, 3, 7]}
# major_student.rate_hw(major_lecturer, 'Python', 5)
print(major_student)

major_student_2 = Student('Anna', 'Popova', 'woman')
major_student_2.courses_in_progress = ['Python', 'Web']
major_student_2.finished_courses = ['С++']
major_student_2.grades = {'Python': [10,5,7], 'Web': [10, 2, 3, 7]}
# major_student_2.rate_hw(major_lecturer_2, 'Boss', 3)
print(major_student_2)

print(major_student > major_student_2)

major_reviewer = Reviewer('Mick', 'Young')
# major_reviewer.rate_hw(major_student, 'Web', 5)
print(major_reviewer)

major_reviewer_2 = Reviewer('Mi', 'You')
# major_reviewer.rate_hw(major_student, 'We', 5)
print(major_reviewer)

all_students = [major_student_2.grades, major_student.grades]
name_course = 'Web'
all_grades = []
length = []
def rate_average_grade_S(student,course):

    for name_student in student:
        all_grades.append(sum(name_student.get(course)))
        length.append(len(name_student.get(course)))
    average_grade = sum(all_grades) / sum(length)
    return round(average_grade,2)

print(f'Cредяя оценка за домашние задания по всем студентам: {rate_average_grade_S(all_students,name_course)}')

all_lecture = [major_lecturer.grades, major_lecturer_2.grades]
name_course = 'Python'
all_grades_l = []
length_l= []
def rate_average_grade_L(lecture,course):

    for name_lecture in lecture:
        all_grades_l.append(sum(name_lecture.get(course)))
        length_l.append(len(name_lecture.get(course)))
    average_grade = sum(all_grades_l) / sum(length_l)
    return round(average_grade,2)

print(f'Cредяя оценка за лекции всех лекторов: {rate_average_grade_L(all_lecture,name_course)}')