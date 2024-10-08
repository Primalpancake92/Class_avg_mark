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


def best_performer(classroom : Classroom):
    """The purpose of this method is to find the best performing student in the classroom
    then return the the student name as the highest achiever of the class.

    Args:
        classroom (Classroom): objects of the classroom class are used

    Returns:
        string: returns the name of the student who achieved the highest mark
    """
    # Initiate the best student variable
    highest_achiever = classroom.class_details[0][3]
    # Iterates through the classroom the highest achiever
    for i in range(classroom.get_class_details()):
        # If current mark exceeds initial highest achiever
        if classroom.class_details[i][3] > highest_achiever:
            # Highest achiever is the current student mark
            highest_achiever = classroom.class_details[i][3]
            # returns the higest achiever of the classroom
            return f"{classroom.class_details[i][0:2]} is the highest achiever with a mark of {highest_achiever}."
            

def worst_performer(classroom : Classroom):
    """Finds the worst performer of the classroom

    Args:
        classroom (Classroom): Takes objects of the classroom as arguments
        
    Returns:
        string (classroom object): Returns the names of the worts students.
    """
    worst_achiever = classroom.class_details[0][3]
    for j in range(classroom.get_class_size()):
        if classroom.class_details[j][3] < worst_achiever:
            worst_achiever = classroom.class_details[j][3]
            formatted = f"{classroom.class_details[j][0:2]} is the worst performing student, with a mark of {worst_achiever}."
            return formatted