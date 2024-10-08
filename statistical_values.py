import statistics
from student import Student
from classroom import Classroom

def mean_mark(student : Student, classroom : Classroom):
    # Declares the total before the for loop
    total = 0
    # Loops and adds the student marks
    for i in range(classroom.get_number_of_students()):
        total += student.get_mark()
    
    # Calculates the mean by dividing the total by the number of students
    mean = total / classroom.get_number_of_students()
    
    # Returns the mean 
    return mean


def best_performer(student: Student, classroom : Classroom):
    # Initiate the best student variable
    highest_achiever = classroom[0][3]
    # Iterates through the classroom the highest achiever
    for i in range(classroom.get_class_details()):
        # If current mark exceeds initial highest achiever
        if classroom[i][3] > highest_achiever:
            # Highest achiever is the current student mark
            highest_achiever = classroom[i][3]
    
    # returns the higest achiever of the classroom
    return classroom[i]