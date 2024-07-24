import sys

def student_parser(user_input: str) -> list[str, str, float] | None:
    user_input = user_input.strip()
    token = user_input.split(" ")
    
    if len(token) != 3:
        print("Formatting error: <student first name> <student last name> <mark>")
        return
        
    first_name, last_name, mark = token
    
    try: 
        mark = float(mark)
    except ValueError:
        print("Error: The student's mark is a number with 2 decimal places")
        return
    
    if not (first_name.isalpha() and last_name.isalpha()):
        print("The first and last name are invalid.")
        return
    elif not (first_name.isalpha() or last_name.isalpha()):
        print("The first or last name are invalid.")
        return
        
    if 0 < mark > 100: 
        print("An overall mark for assessments are from 0 to 100.")
        return
    elif 0 < mark > 100 and not (first_name.isalpha() or last_name.isalpha()):
        print("Invalid mark and first or last name.")
        return
    elif 0 < mark > 100 and not (first_name.isalpha() and last_name.isalpha()):
        print("Invalid mark and first and last name.")
        return
    
    return [first_name, last_name, mark]
