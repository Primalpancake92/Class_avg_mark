from student import Student
from teacher import Teacher

class Classroom:
    def __init__(self, class_ID: int, class_size: int, number_of_students: int):
        """This is where all student objects will be stored and remains as an
        associative entity for the students. This constructor instantiates 
        this class type.

        Args:
            class_ID (int): This is the primary identifier of the classroom
            class_size (int): Represents the size of the classroom
            number_of_students (int): Number of students in the classroom
        """
        self.class_ID = class_ID
        self.class_size = class_size
        self.number_of_students = number_of_students
        self.teacher_assigned = None
        self.class_details = []
    
    
    def set_class_ID(self, class_ID):
        """Sets the ID of the classroom to the instance.

        Args:
            class_ID (int): _description_
        """
        self.class_ID = class_ID
        
    
    def set_class_size(self, class_size):
        self.class_size = class_size
    
    
    def get_class_size(self):
        return self.class_size
    
    
    def get_class_ID(self):
        return self.class_ID
    
    
    def get_class_details(self):
        return self.class_details
        
        
    def get_student_details(self):
        formatted = ""
        if not self.class_details:
            return "Your classroom is empty. Let's add some students!"
        for i in range(len(self.class_details)):
            formatted += f"\nName: {self.class_details[i][0]} {self.class_details[i][1]}\nAge: {self.class_details[i][2]}\nMark: {self.class_details[i][3]}\nGrade: {self.class_details[i][4]}\n"
        return formatted


    def get_number_of_students(self):
        """Counts the number of students that are in the classroom.
        
        Does not have any arguments as it refers to the object's attributes.
        """
        return len(self.class_details)
        
        
    def adding_students(self, student : Student):     
        if len(self.class_details) > self.class_size:
            raise ValueError("There are too many students in your class.")
        else:
            self.class_details.append(student.get_summary())

    
    def remove_student(self, student : Student):
        for i in range(len(self.class_details)):
            if self.class_details[i] == student:
                self.class_details.remove(self.class_details[i])
                break
    
    
    def students_update(self):
        if self.remove_student(): 
            self.number_of_students -= 1
        elif self.adding_students():
            self.number_of_students += 1
        
    
    def finding_student(self, student: Student):
        for i in range(len(self.class_details)):
            if self.class_details[i] == student:
                return True
            return False
    

    def student_found_or_not(self, student : Student):
        if self.finding_student(student) == True:
            return f"{student.get_first_name} {student.get_last_name()} found in {self.get_class_ID()}."
        return f"{student.get_first_name} {student.get_last_name()} not found in {self.get_class_ID()}."
    
    
    def assign_teacher(self, teacher : Teacher):
        if self.teacher_assigned is not None:
            raise ValueError(f"{self.class_ID} is already assigned to teacher {teacher.get_teacher_ID()}.")
        self.teacher_assigned = teacher
        
        
    def calculating_grades(self, student : Student):
        grades = ("HD", "D", "C", "P", "F")
            
        for i in range(len(self.class_details)):
            if 85 <= student.get_mark() <= 100:
                self.class_details[i][4] = grades[0]
                student.grade = grades[0]
            elif 75 <= student.get_mark()<= 84: 
                self.class_details[i][4] = grades[1]
            elif 65 <= student.get_mark()<= 74:
                self.class_details[i][4] = grades[2]
            elif 64 <= student.get_mark()<= 50:
                self.class_details[i][4] = grades[3]
            elif student.get_mark()< 50:
                self.class_details[i][4] = grades[4]
         
    
    def __str__(self) -> str:
        formatted = f"\nClass ID: {self.get_class_ID()}\nClass size: {self.get_class_size()}\nNumber of students: {self.get_number_of_students()}\nList of students: {self.get_class_details()}"
        return formatted