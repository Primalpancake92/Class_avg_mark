from classroom import Classroom
from student import Student
import math

def mean_mark(classroom : Classroom) -> float:
    total = 0
    for student in classroom.class_details:
        total += student[3]
    
    mean = total / len(classroom.class_details)
    
    return mean


def class_median(classroom : Classroom) -> int:
    list_of_marks = []
    
    for student in classroom.class_details:
        list_of_marks.append(student[3])

    # Using selection sort
    n = len(list_of_marks)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if list_of_marks[j] < list_of_marks[min_index]:
                min_index = j

        if min_index != i:
            list_of_marks[i], list_of_marks[min_index] = list_of_marks[min_index], list_of_marks[i]       

    mid_point = n // 2
    
    if n % 2 == 0:
        median = (list_of_marks[mid_point - 1] + list_of_marks[mid_point]) / 2
    else:
        median = (list_of_marks[mid_point])
    
    return median


def std_deviation(classroom : Classroom) -> float:
    divisor = len(classroom.class_details) - 1
    dividend = 0

    for student in classroom.class_details:
        dividend += (student[3] - mean_mark(classroom)) ** 2 
    
    std_dev = math.sqrt(dividend / divisor)
    
    return f"{std_dev:.2f}"


def variance(classroom : Classroom):
    dividend = 0
    divisor = len(classroom.class_details) - 1
    
    for student in classroom.class_details:
        dividend += (student[3] - mean_mark(classroom)) ** 2
    
    var = (dividend) / divisor
    
    return f"{var:.2f}"


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


def summary(classroom : Classroom):
    best = best_student(classroom)
    worst = worst_student(classroom)
    best_in_text = f"{best[0]} {best[1]} ({best[3]})"
    worst_in_text = f"{worst[0]} {worst[1]} ({worst[3]})"
    
    summary_text = (
        "=" * 56 + "\n" +
        "Summary Statistics".center(56) + "\n" +
        "=" * 56 + "\n" +
        f"{'Statistic'.center(28)}{'Value'.center(28)}\n" +
        "-" * 56 + "\n" +
        f"{'Mean':<30}{mean_mark(classroom):>26.2f}\n" +
        f"{'Median':<30}{class_median(classroom):>26.2f}\n" +
        f"{'Standard Deviation':<30}{std_deviation(classroom):>26}\n" +
        f"{'Variance':<30}{variance(classroom):>26}\n" +
        f"{'Best Student':<30}{best_in_text:>26}\n" +
        f"{'Worst Student':<30}{worst_in_text:>26}\n" +
        "=" * 56
    )
    return summary_text