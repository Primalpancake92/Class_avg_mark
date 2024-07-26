import sys
import math
from art import text2art
from input_parser import student_parser

'''
This is the main file of the class average mark. The purpose of this project is to build a script that is able to take inputs from the user, in the form of marks in respect 
to student names. Ultimately, the user will be able to easily calculate the overall mark of the class. 

In future iterations, we could include other statistical values that can be calculated from this script.
'''
def banner():
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


def student_data(data: list) -> list:
    while True:
        student_data = input("Please enter student name and mark for your class: ").strip()
        if student_data == "Done!":
            break
        if student_data:
            data_parsed = student_parser(student_data)
            if data_parsed is not None:
                data.append(data_parsed)
        if not student_data:
            print("You have not entered anything. Please enter <first name> <last name> <mark>.")
                
    
def class_input():
    student_list = []
    what_calculate = input("\nWhat would you like to assess? ")
    if what_calculate.capitalize() == "Nothing else":
        print("It was nice working with you. Have a good day!")
        sys.exit(0)
    if what_calculate.capitalize() == "Help":
        print('''\nThis prompt is to ask you what you would like to calculate for the class.
This could be the class marks, final exams, assessments, and attendance. 
It can be whateveer you would like. This is not just limited to marks alone. 
It could calculate anything. Just type it in and the calculator will find it 
out for you.''')
    if what_calculate and (what_calculate.capitalize() != "Help" and what_calculate.capitalize() != "Nothing else"):
        student_data(student_list)
        print(f"Your class is: {student_list}")
        while True:
            data_type = input("What would you like to calculate from the class? ")
            if data_type == "Nothing else":
                print("It was nice working with you. Have a good day or night.")
                break
            if data_type == "Help":
                print('''\nHere are the following prompts you may use to let me help you out:
- 'Average' or 'Mean'
- 'Max'
- 'Min'\n''')
            if data_type == "Average" or data_type == "Mean": 
                print(f"The class average {what_calculate} marks is: {class_avg_mark(student_list)}")
            if data_type == "Median":
                print(f"The class average {what_calculate} marks is: {class_median(student_list)}")
            if data_type == "Max":
                print(f'The highest achieving student was {class_max_mark(student_list)}')
            if data_type == "Min":
                print(f"The lowest achieving student was {class_min_mark(student_list)}")
            

def class_avg_mark(students: list) -> float:
    if len(students) != 0:
        total = sum(mark for _, _, mark in students)  # calculates the total mark from the length of te list.
        return total/len(students) # then returns the average
    
    return 0.0 # if there is no entries in the list, then return 0


def class_median(students: list) -> float:
    if not students:
        return "There are no students in your class."

    marks = sorted(student[2] for student in students)
    
    n = len(marks)
    mid = n // 2
    
    if n % 2 == 1:
        # If odd, return the middle mark
        median = marks[mid]
    else:
        # If even, return the average of the two middle marks
        median = (marks[mid - 1] + marks[mid]) / 2
    
    return median

            
def class_max_mark(students: list) -> StopIteration:
    max_mark = students[0][2]
    max_student_mark = students[0]
    i = 0 
    while i < len(students):
        if students[i][2] > max_mark:
            max_mark = students[i][2]
            max_student_mark = students[i]
        i += 1
    return f"{max_student_mark[0]} {max_student_mark[1]}, with a mark of {max_mark:.2f}."


def class_min_mark(students: list) -> float:
    min_mark = students[0][2]
    min_student_mark = students[0]
    i = 0 
    while i < len(students):
        if students[i][2] < min_mark:
            min_mark = students[i][2]
            min_student_mark = students[i]
        i += 1
    return f"{min_student_mark[0]} {min_student_mark[1]} with a mark of {min_mark:.2f}"


def std_dev(students: list) -> float:
    mean = class_avg_mark(students)
    n = len(students)
    
    diff = 0
    i = 0 
    while i < len(students):
        diff += (students[i][2] - mean) ** 2
        i += 1
    
    std_dev = math.sqrt((1 / n) * diff)
    return std_dev


def std_err(students: list) -> float:
    n = len(students) # number of samples or the length of the list
    error = std_dev(students) / math.sqrt(n) # Finds the standard error using standard deviation over the square root of samples
    
    return error #returns float value


def main():
    print(banner())
    class_input()


if __name__ == "__main__":
    main()
    