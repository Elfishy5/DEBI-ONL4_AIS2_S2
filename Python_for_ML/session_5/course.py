class Course :
    id_counter = 1
    def __init__(self,name):
        self.course_id = Course.id_counter
        Course.id_counter += 1
        self.name = name
        self.enrolled_students = []

    def __repr__(self):
        return f"course ID : {self.course_id} , Name = {self.name} , Enrolled : {len(self.enrolled_students)}"    
    
    def enroll_students(self,student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print ("Student enrolled successfully!")
        else:
            print("Student already enrolled!")    
    
    def remove_student(self,student) :
        if student in self.enrolled_students :
            self.enrolled_students.remove(student)
            print("Student removed successfully!")
        else :
            print("Student not found in this course")    
