class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Example usage
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

course = Course("Computer Science")

course.add_student(student1)
course.add_student(student2)

print("Course:", course.name)

for student in course.students:
    print(student.name, "-", student.student_id)