from classroom import Classroom
from student import Student
from teacher import Teacher
import input_parser
import statistical_values 
from art import text2art


def startup_screen():
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


'''def program_start():
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

    print(classroom.get_student_details())'''
    

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
            # show that the classroom details have been added
            print("Classroom details have been added.\n")
            break
    # instantiation of the classroom object using previous user input
    classroom = Classroom(class_input[0], class_input[1], class_input[2])
    
    # if there are no members of the classrom list
    if len(classroom.class_details) == 0:
        # say that there are no students
        print("There are no students in your classroom.")
        # provide the user with the option to add students
        add_students = input("Would you like to add some students? ")
        # while the user does not input done keep asking for input
        while add_students.lower() != "done":
            # if the user inputs yes
            if add_students.lower().strip() == "yes":
                # enter this students' details
                adding_students = input("Enter student details here: ")
                # parse this input through its respective method
                parsed_students = input_parser.parse_students(adding_students)
                # if there is a return value
                if parsed_students is not None:
                    # instantiate the object
                    student = Student(parsed_students[0], parsed_students[1], parsed_students[2], parsed_students[3], parsed_students[4])
                    classroom.adding_students(student)
                    print(f"{student}\n")
                    print(f"{str(classroom.get_class_details())}")
            else: 
                continue
            
        
if __name__ == "__main__":
    print(startup_screen())
    input_gathering()
    