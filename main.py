class Student:
    # count = 0
    student_list = []
    student_grade = []
    courses_in_progress = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # Student.count += 1
        Student.student_list.append(surname + " " + name)
        Student.student_grade.append(self.grades)
        Student.courses_in_progress.append(self.courses_in_progress)

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grade(self):
        count = 0
        sum_values = 0
        for keys, values in self.grades.items():
            sum_values += sum(values)
            count += len(values)
        if count != 0:
            avg_values_full = sum_values / count
        return avg_values_full

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {round(Student.__avg_grade(self), 1)} ' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}  \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        elif self.__avg_grade() > other.__avg_grade():
            print(
                f'У студента {self.name} {self.surname} средняя оценка больше, чем у студента {other.name} {other.surname}')
        else:
            print(
                f'У студента {other.name} {other.surname} средняя оценка больше, чем у студента {self.name} {self.surname}')
        return self.__avg_grade() > other.__avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    lecturer_grade = []
    courses_attached = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []  # добавил список курсов
        Lecturer.lecturer_list.append(surname + " " + name)
        Lecturer.lecturer_grade.append(self.grades)
        Lecturer.courses_attached.append(self.courses_attached)
        # self.avg = []  # добавил

    def __avg(self):
        count = 0
        sum_values = 0
        for keys, values in self.grades.items():
            sum_values += sum(values)
            count += len(values)
        if count != 0:
            avg_values_full = sum_values / count
        return avg_values_full

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(Lecturer.__avg(self), 1)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        return self.__avg() < other.__avg()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


first_student = Student('Ruoy', 'Eman', 'your_gender')
second_student = Student('Alex', 'Trey', 'your_gender')

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer = Reviewer('Lyla', 'Lepinscy')
second_reviewer.courses_attached += ['Python', 'Git']

first_lecturer = Lecturer('Petr', 'Gudima')
second_lecturer = Lecturer('Filip', 'Morris')

first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Введение в программирование']

second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['Введение в программирование']

first_lecturer.courses_attached += ['Python', 'Git']
second_lecturer.courses_attached += ['Python', 'Git']

first_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 8)

first_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Python', 9)

first_student.rate_lw(first_lecturer, 'Python', 8)
first_student.rate_lw(second_lecturer, 'Python', 10)

second_student.rate_lw(first_lecturer, 'Git', 9)
second_student.rate_lw(second_lecturer, 'Git', 10)

print("Задание №2")
print()
print('reviewer')
print(second_reviewer)
print()
print('lecturer')
print(second_lecturer)
print()
print('student')
print(second_student)
print()
print('student')
print(first_student)
print()
second_student > first_student
print()

# Задание №4
print("Задание №4")
print()
print("Cредние оценки за домашние задания по всем студентам в рамках конкретного курса:")
print()


# Функция для студентов

def avg_grade_student(student_list, course):  # функция

    if course not in Student.courses_in_progress[0]:
        print("Нет такого курса!")
    else:
        count = 0
        for i in range(len(student_list)):
            for n in range(i, i + 1):
                avg_grade = sum(Student.student_grade[count].get(course, None)) / len(
                    Student.student_grade[count].get(course, None))
            print(
                f'курс обучения {course}; фамилия и имя студента: {student_list[count]}; средняя оценка по курсу: {avg_grade}')
            count += 1


avg_grade_student(Student.student_list, "Python")

print()
print("Cредние оценки за лекции всех лекторов в рамках курса:")
print()


# Функция для лекторов

def avg_grade_lecturer(lecturer_list, course):  # функция

    if course not in Lecturer.courses_attached[0]:
        print("Нет такого курса!")
    else:
        count = 0
        for i in range(len(lecturer_list)):
            for n in range(i, i + 1):
                avg_grade = sum(Lecturer.lecturer_grade[count].get(course, None)) / len(
                    Lecturer.lecturer_grade[count].get(course, None))
            print(
                f'курс преподавания {course}; фамилия и имя лектора: {lecturer_list[count]}; средняя оценка по курсу: {avg_grade}')
            count += 1


avg_grade_lecturer(Lecturer.lecturer_list, "Git")
