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
    while True:
        try:
            class_ID, class_size, number = input("\nEnter the details of the classroom: ").split(" ")
            token = class_ID, class_size, number
            
            if not (class_ID.isdigit() and class_size.isdigit() and number.isdigit()):
                raise ValueError("Class ID, class size, and number of students must all be a numerical number.")
            
            class_ID = int(class_ID)
            class_size = int(class_size)
            number = int(number)
            
            classroom = Classroom(class_ID, class_size, number)
            
            
            print(classroom.__str__())
            
            if len(classroom.class_details) == 0:
                print("\nThere seems to be no students in your classroom.\n")
            
            if token == "end program":
                break
            
        except ValueError as e:
            print(e)
        
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

            classroom.adding_students(students)
            classroom.calculating_grades(students)
            i += 1
            
        except ValueError:
            print("Note that the Student ID, age and mark must be a number. Please enter again.")

    print(classroom.get_student_details())


if __name__ == "__main__":
    print(startup_screen())
    program_start()
    