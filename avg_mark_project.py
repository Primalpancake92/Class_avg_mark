import sys
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
            if data_type == "Help":
                print('''\nHere are the following prompts you may use to let me help you out:
- 'Average' or 'Mean'
- 'Max'
- 'Min'\n''')
            if data_type == "Average" or data_type == "Mean": 
                print(f"The class average {what_calculate} marks is: {class_avg_mark(student_list)}")
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
    students[2].sort()
    n = len(students)
    if n % 2 == 1:
        median = students[n // 2]
    else:
        median = (students[n // 2 - 1] + students[n // 2]) / 2
    return median
            

def class_max_mark(students: list) -> StopIteration:
    i = 0  
    while i < len(students):
        max_achieve = students[0]
        if students[i] > max_achieve:
            max_achieve = students[i]
        i += 1
    return f"{max_achieve[0]} {max_achieve[1]}, with a mark of {max_achieve[2]:.2f}."


def class_min_mark(students: list) -> float:
    i = 0 
    while i < len(students):
        min = students[0]
        if students[i] < min:
            min = students[i]
        i += 1
    return f"{min[0]} {min[1]}, with a mark of {min[2]:.2f}."
    

def main():
    print(banner())
    class_input()


if __name__ == "__main__":
    main()
