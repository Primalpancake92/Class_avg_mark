def parse_class_details(input: str) -> tuple[int, int, int] | None:
    tokens = input.split(" ")
    
    if len(tokens) != 3:
        print("""There are too many or to little arguments.
<classroom ID> <classroom size> <number of 
students enrolled in the classroom>""")
        return
    
    class_ID, class_size, students_enrolled = tokens
    
    if len(class_ID) != 3:
        print("The class ID number only has 3 digits.")
        return
        
    try: 
        class_ID = int(class_ID)
        
    except ValueError :
        if not class_ID.isdigit():
            print("Error: please enter class ID as a number.")
        return 

    try:
        class_size = int(class_size)
        
    except ValueError as e:
        if not class_size.isdigit():
            print("Error: please enter the class size as a number.")
        return
    
    try:
        students_enrolled = int(students_enrolled)
        
    except ValueError:
        if not students_enrolled.isdigit():
            print("Error: please enter the number of students enrolled as a number.")
        if students_enrolled > class_size:
            print("Error: there are more students than the classroom permits.")
        return
    
    return class_ID, class_size, students_enrolled


def parse_students(student_input: str) -> list[int, str, str, int, float]:
    tokens = student_input.split(" ")
    
    if len(tokens) != 5:
        print("Error: <student ID> <student first name> <student last name> <student age> <student mark>")
        return
    
    student_id, first_name, last_name, age, mark = tokens
    
    try:
        student_id = int(student_id)
        first_name = str(first_name)
        last_name = str(last_name)
        age = int(age)
        mark = float(mark)
        
    except ValueError:
        if not student_id.isdigit(): 
            print("Error: enter a valid student ID.")
            return
        if not isinstance(first_name, str):
            print("Error: enter a valid first name for the student.")
            return
        if not isinstance(last_name, str):
            print("Error: enter a valid last name for the student.")
            return
        if not age.isdigit():
            print("Error: enter a valid age.")
            return
        if not isinstance(mark, float):
            print("Error: enter a valid mark.")
            return
    
    return student_id, first_name, last_name, age, mark