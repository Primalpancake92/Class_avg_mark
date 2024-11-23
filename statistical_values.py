from classroom import Classroom
from student import Student


def mean_mark(classroom : Classroom) -> int:
    total = 0
    for student in classroom.class_details:
        total += student[3]
    
    mean = total / len(classroom)
    
    return f"The class mean is: {mean}"


def best_student(classroom : Classroom) -> list[Student]:
    best_student = classroom.class_details[0]
    best_mark = 0
    
    for student in classroom.class_details:
        if student[3] > best_mark:
            best_mark = student[3]
            best_student = student

    return best_student


def worst_student(classroom : Classroom) -> list[Student]:
    worst_student = classroom.class_details[0]
    worst_mark = 100
    
    for student in classroom.class_details:
        if student[3] < worst_mark:
            worst_mark = student[3]
            worst_student = student
        
    return worst_student