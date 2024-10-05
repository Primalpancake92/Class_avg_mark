class Teacher:
    def __init__(self, teacher_ID: int, first_name: str, last_name: str):
        """This class constructor instantiates the teachers that are possibly
        assigned to each instance of each Classroom. 

        Args:
            teacher_ID (int): ID number of the teacher - A key identifier
            first_name (str): First name of the teacher
            last_name (str): Last name of the teacher
        """
        self.teacher_ID = teacher_ID
        self.first_name = first_name
        self.last_name = last_name
        self.assigned_classroom = None

    
    def set_teacher_ID(self, teacher_ID):
        self.teacher_ID = teacher_ID
        
    
    def set_t_first_name(self, first_name):
        self.first_name = first_name
    
    
    def set_t_last_name(self, last_name):
        self.last_name = last_name
    
    
    def get_teacher_ID(self):
        return self.teacher_ID

    
    def get_teacher_firstn(self):
        return self.first_name
    
    
    def get_teacher_lastn(self):
        return self.last_name
        