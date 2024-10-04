class Student:
    def __init__(self, first_name: str, last_name: str, age: int, mark: float, grade: str):
        """
        Instantiates each and every student that belongs to this class. 
            
        They are given the following parameters: 
            - First name: represented as a string
            - Last name: represented as a string
            - Age: represented as an integer
            - Mark: represented as a float value
            - Grade: represented as a string
    
        This is an entity that describes the information and attributes of the student,
        which is done so by the above mentioned parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mark =  mark
        self.grade = grade
        

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    
    def set_age(self, age):
        """This sets or even updates the age of the student

        Arguments:
           age (int): This represents the age of the student
        """
        self.age = age
        
    
    def set_grade(self):
        self.grade = Student.calculate_grade(self.mark)
        
    
    def set_mark(self, mark):
        self.mark = mark
    
    
    def get_first_name(self):
        return self.first_name
        
        
    def get_last_name(self):
        return self.last_name
    
    
    def get_mark(self):
        return self.mark


    def get_age(self):
        return self.age
    
    
    def get_grade(self):
        return self.grade
        
    
    def get_summary(self): # Returns a list of summary values of the parameters in the student objects.
        summary = [self.get_first_name(), self.get_last_name(), self.get_age(), self.get_mark(), self.get_grade()]
        
        return summary
        
    
    def calculate_grade(mark):
        uni_grades = ("HD", "D", "C", "P", "F")
        
        # high_school_grading_scale = {"A", "B", "C", "D", "E"} 
        # This is consideration of the high school iteration of this application.
        
        if 0 <= mark <= 49:
            return uni_grades[4]
        elif 50 <= mark <= 64:
            return uni_grades[3]
        elif 65 <= mark <= 74:
            return uni_grades[2]
        elif 75 <= mark <= 84:
            return uni_grades[1]
        elif 85 <= mark <= 100:
            return uni_grades[0]
        
        
    def __str__(self) -> str:
        formatted = f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nMark: {self.mark}\nGrade: {self.grade}"
        
        return formatted
    

if __name__ == "__main__":
    student1 = Student("Alice", "Smith", 18, 85.0, "A")
    
    student1.set_name("Wanker", "Jerkoff")
    print(student1.get_first_name())
    print(student1.get_last_name())
    student1.set_mark(100)
    print(student1)
    print(student1.get_summary())