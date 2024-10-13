class Member:
    def __init__(self, name, age, status, subject):
        self.name = name
        self.age = age

        self.status = status
        self.subject = subject


class Teacher(Member):
    def __init__(self, name, age, status, subject, salary):
        super().__init__(self, name, age, status, subject)
        self.salary = salary

    def calculate_year_salary(self):
        return 12 * self.salary


        
class Student(Member):
    def __init__(self, name, age, status, subject, grade):
        super().__init__(self, name, age, status, subject)
        self.grade = grade

    def __str__(self):
        return f"name: {self.name}"
c

sani = Teacher("sani", 16, "teacher", "py" , 1000000)

