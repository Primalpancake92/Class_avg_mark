from classroom import Classroom

def parse_class_details(input: str) -> tuple[int, int, int] | None:
    tokens = input.split(" ")
    
    if len(tokens) != 3:
        print("""There are too many or to little arguments.
              <classroom ID> <classroom size> <number of 
              students enrolled in the classroom>""")
        return
    
    class_ID, class_size, students_enrolled = tokens
        
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