class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def introduce(self):
        old_introduce = super().introduce()
        return old_introduce + "I am a student"

student = Student("Joey", "Bizinger")
print(student.introduce())

