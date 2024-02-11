

class Student:

    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        
    def get_courses(self):
        print(f"Registered courses: {', '.join(self.courses)}")

    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f"{course_name} has been added to {self.name}s courses")

    def remove_course(self, course_name):
        self.courses.remove(course_name)
        print(f"{course_name} has been removed from {self.name}s courses")



student1 = Student("Nika", 1, ["History", "Geography", "Science"])

student1.get_info()
student1.get_courses()
student1.add_course("Economics")
student1.remove_course("History")
student1.get_courses()

student2 = Student("Giorgi", 2, ["German", "Programming", "Chemistry", "English"])
student2.get_info()
student2.get_courses()
student2.add_course("Spanish")
student2.add_course("Biology")
student2.get_courses()
student2.remove_course("English")
student2.get_courses()