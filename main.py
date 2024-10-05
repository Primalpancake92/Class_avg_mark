from classroom import Classroom
from student import Student
from teacher import Teacher
import statistical_values 
from art import text2art


def startup_screen():
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


def program_start():
    print(startup_screen())
    i = 0
    while True:
        token = input("Enter Student details: ")
        if token == "I am done":
            break
            
        try:
            SID, first_name, last_name, age, mark = token.split(" ")

            SID = int(SID)
            age = int(age)
            mark = float(mark)
            
            students = Student(SID, first_name, last_name, age, mark)
            
            print(students.get_summary())
        
        except ValueError:
            print("Note that the Student ID, age and mark must be a number. Please enter again.")
        
    
        
    

if __name__ == "__main__":
    program_start()