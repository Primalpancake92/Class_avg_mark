from classroom import Classroom
from student import Student
from teacher import Teacher
import statistical_values 
import text2art


def startup_screen():
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


def program_start():