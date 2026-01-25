class Student:
    id_counter = 1

    def __init__(self,name):
        self.student_id=Student.id_counter
        Student.id_counter+=1
        self.name=name
        self.grades={}
        self.enrolled_courses=[]

    def __str__(self):
        return f"Student ID : {self.student_id},Name : {self.name},Grades : {self.grades}" 

    def __repr__(self):
        return f"Student ID : {self.student_id},Name : {self.name},Grades : {self.grades}"    

    def add_grade(self,course_id,grade):
        self.grades[course_id] = grade

    def enroll_in_course(self,course):
        self.enrolled_courses.append(course)