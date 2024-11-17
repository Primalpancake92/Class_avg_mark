from classroom import Classroom
from student import Student
from teacher import Teacher
import input_parser
import statistical_values 
from art import text2art

def startup_screen():
    """
    This method prints out the banner of the program.
    """
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


def input_gathering():
    """
    Gathers user input for adding the details fof the classroom and student objects.
    Before doing so, the inputs are split and parsed through the input_parser.py file.
    Once it returns the inputs, which are not none, these objects are instantiatied.
    """
    print("Time to create our classroom!") # prints out a statement notifying the user
    # when this is always true
    while True: 
        # ask user for input
        class_details_input = input("Enter the details of the classroom: ").strip() # removes white space from input
        # parses these inputs through its respective method
        class_input = input_parser.parse_class_details(class_details_input)
        # if there is a return value
        if class_input is not None:
            # instantiates user inputs as classroom objects
            classroom = Classroom(class_input[0], class_input[1], class_input[2])
            # show that the classroom details have been added
            print("Classroom details have been added.\n")
            break
        
    
    # if there are no members of the classrom list
    if not classroom.class_details:
        # say that there are no students
        print("There are no students in your classroom.")
        
        while True: 
            student_add = input("Would you like to add some students? ")
            if student_add.lower().strip() == "done":
                # prints goodbye message
                print("Goodbye. Have a good day!")
                return
            elif student_add.lower().strip() == "yes":
                adding_students_to_classroom(classroom)
                break
            else: 
                print("Sorry I do not understand what you are trying to do.")
            

def adding_students_to_classroom(classroom : Classroom):
    while True:
        adding_students = input("Please enter student details: ")
        if adding_students.lower().strip() == "i am done":
            print("All students have been added successfully.")
            print(f"This is the classroom:\n{classroom.get_class_details()}")
            return
        parsed_students = input_parser.parse_students(adding_students)
        if parsed_students is not None:
            # instantiate the object
            student = Student(parsed_students[0], parsed_students[1], parsed_students[2], parsed_students[3], parsed_students[4])
            classroom.adding_students(student)
            print(f"{student.get_first_name()} {student.get_last_name()} was added.")
        else: 
            print("I am sorry, I do not konw what you are trying to say.")
        

def key_performance():
    """
    The purpose of this method is to prompt the user with some options, so they
    can analyse the classroom and get key performance indicators of the class-
    room.

    Return
    """
    types = input("What would you like to find out about the classroom? ")
    
    
        
if __name__ == "__main__":
    print(startup_screen())
    input_gathering()
    key_performance()