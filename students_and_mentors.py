class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # среднее за домашние задания
    def average(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        average_rating = sum(map(sum, self.grades.values())) / grades_count
        return round(average_rating)

    def __str__(self):
         courses_in_progress_string = ', '.join(self.courses_in_progress)
         finished_courses_string = ', '.join(self.finished_courses)
         res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
         return res

    # оценки лекторам
    def grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                (course in self.courses_in_progress or course in self.finished_courses)\
                and 0 < round(grade) <=10:
            if course in lecturer.grades:
                lecturer.grades[course] += [round(grade)]
            else:
                lecturer.grades[course] = [round(grade)]
        else:
            return 'Ошибка'

    # сравнение студентов по средней за домашнее задание
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average() < other.average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # считаем среднее за лекции
    def average_rating(self):
        grades_count = 0
        average = float()
        for k in self.grades:
            grades_count += len(self.grades[k])
        average = sum(map(sum, self.grades.values())) / grades_count
        return round(average)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
             f'Фамилия: {self.surname} \n'\
             f'Средняя оценка за лекции: {self.average_rating()}'
        return res

    # сравнение лекторов по средней за лекции
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating() < other.average_rating()



class Reviewer(Mentor):
    # оценки студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and (course in student.courses_in_progress or student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
                f'Фамилия: {self.surname}'
        return res


# создаем объект Student
student_1 = Student('Петр', 'Петров', 'your_gender')
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Ci']

student_2 = Student('Иван', 'Иванов', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Ci']


# создаем объект Lecturer
lector_1 = Lecturer('Larry', 'Baks')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['Ci']
lector_1.courses_attached += ['Java']

lector_2 = Lecturer('Piter', 'Barr')
lector_2.courses_attached += ['Python']
lector_2.courses_attached += ['Ci']
lector_2.courses_attached += ['Java']


# вызываем метод выставления оценок Лекторам
student_1.grades_lecturer(lector_1, 'Python', 1)
student_1.grades_lecturer(lector_1, 'Ci', 9)
student_1.grades_lecturer(lector_1, 'Java', 5)

student_2.grades_lecturer(lector_2, 'Python', 3)
student_2.grades_lecturer(lector_2, 'Ci', 2)
student_2.grades_lecturer(lector_2, 'Java', 5)

# создаем объект  Reviewer
reviewer_1 = Reviewer('Piter', 'Buxin')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Ci']

reviewer_2 = Reviewer('Ivan', 'Lopuxin')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']
reviewer_1.courses_attached += ['Ci']

reviewer_1.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Ci', 2)
reviewer_1.rate_hw(student_1, 'Java', 3)

reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Ci', 5)
reviewer_2.rate_hw(student_2, 'Java', 6)


print(lector_1)
print(lector_2)

print(reviewer_1)
print(reviewer_2)

print(student_1)
print(student_2)

# сравниваем студентов
print(f'Результат сравнения студентов: '
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# сравниваем лекторов
print(f'Результат сравнения лекторов: '
      f'{lector_1.name} {lector_1.surname} > {lector_2.name} {lector_2.surname} = {lector_1 > lector_2}')
print()

#*********************************************************************
# Создаем список студентов
student_list = [student_1, student_2]

# Создаем список лекторов
lecturer_list = [lector_1, lector_2]



def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       for key in stud.grades:
           if key == course_name:
                sum_all += sum(stud.grades[key])
                count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# # Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
# # в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        for key in lect.grades:
            # print('1----',key,'2----',course_name)
            if key == course_name:
                sum_all += sum(lect.grades[key])
                count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()