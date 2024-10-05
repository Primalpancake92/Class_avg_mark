import statistics
from classroom import Classroom

def mean(classroom : Classroom):
    total = 0
    for i in range(classroom.get_number_of_students()):
        total += classroom.class_details[i][4]
        
    return total / classroom.get_number_of_students()
    
        