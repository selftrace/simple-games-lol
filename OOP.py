class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    
    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")

        avg = self.calculate_average()
        print(f"Average: {avg:.2f}")

        if avg >= 50:
            if avg >= 90:
                evaluation = "Excellent"
            elif avg >= 75:
                evaluation = "Good"
            else:
                evaluation = "Pass"
        else:
            evaluation = "Fail"

        print(f"Evaluation: {evaluation}")
        print("-" * 40)


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject

    def display_info(self):
        print("Teacher Info:")
        super().display_info()
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Subject: {self.subject}")

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        print("-" * 40)
        print("--- Students List ---")
        for s in self.students:
            s.display_info()

    def calculate_class_average(self):
        if not self.students:
            return 0
        total = 0
        for s in self.students:
            total += s.calculate_average()
        return total / len(self.students)

dr_ahmed = Teacher("Dr. Ahmed", 45, "T100", "Computer Science")

s1 = Student("Ali", 20, "S001")
s2 = Student("Sara", 21, "S002")
s3 = Student("Omar", 19, "S003")

s1.add_grade(85);
s1.add_grade(90);
s1.add_grade(88)
s2.add_grade(70);
s2.add_grade(75);
s2.add_grade(72)
s3.add_grade(40);
s3.add_grade(50);
s3.add_grade(45)

my_course = Course("Intro to Python", dr_ahmed)
my_course.add_student(s1)
my_course.add_student(s2)
my_course.add_student(s3)

print(f"Course: {my_course.course_name}")
dr_ahmed.display_info()
my_course.show_all_students()

class_avg = my_course.calculate_class_average()
print(f"Class Average: {class_avg:.2f}")
