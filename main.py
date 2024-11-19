class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def calculate_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(avg_grade, 1)}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(avg_grade, 1)}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()

def average_grade_for_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0


def average_grade_for_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0


student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.grades = {'Python': [10, 9], 'Git': [8, 7]}

student2 = Student('Jane', 'Doe', 'female')
student2.courses_in_progress += ['Python', 'Git']
student2.grades = {'Python': [9, 8], 'Git': [10, 10]}

reviewer1 = Reviewer('John', 'Smith')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Emily', 'Johnson')
reviewer2.courses_attached += ['Git']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 10)

lecturer1 = Lecturer('Dr.', 'Brown')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [10, 9, 8]}

lecturer2 = Lecturer('Prof.', 'Green')
lecturer2.courses_attached += ['Git']
lecturer2.grades = {'Git': [9, 10, 9]}

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Python: {average_grade_for_students(students, 'Python'):.2f}")
print(f"Средняя оценка за лекции по курсу Git: {average_grade_for_lecturers(lecturers, 'Git'):.2f}")

print("\nСтуденты:")
print(student1)
print(student2)

print("\nПроверяющие:")
print(reviewer1)
print(reviewer2)

print("\nЛекторы:")
print(lecturer1)
print(lecturer2)


