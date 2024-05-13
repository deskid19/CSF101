class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students' assignments.")

    def attend_meeting(self):
        print(f"{self.name} is attending a department meeting.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying for exams.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")


# Creating objects
teacher1 = Teacher("Mr. Johnson", 35, "T001", "Mathematics", 60000, "Math Dept", "Senior Lecturer")
student1 = Student("Emma", 20, "S001", "ST001", "Computer Science", 2, 3.8)

# Accessing specific behaviors and attributes
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()

student1.study()
student1.attend_class()
student1.write_exam()

# Accessing common behaviors
teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()

student1.walk()
student1.talk()
student1.eat()
student1.sleep()
