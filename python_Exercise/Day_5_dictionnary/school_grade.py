class School:
    def __init__(self):
        self.students = []
        self.is_added = []

    def add_student(self, name, grade):
        student = {"name" : name, "grade" : grade}
        is_already_student = any(
            std["name"] == name
            for std in self.students
        )
             
        if not is_already_student :
            self.students.append(student)
        self.is_added.append(not is_already_student)

    def roster(self):
        return [student["name"] 
                for student in sorted(self.students, key =lambda s:( s["grade"], s["name"]))]

    def grade(self, grade_number):
        return sorted(student["name"] 
                      for student in self.students
                      if student["grade"] == grade_number)

    def added(self):
        return self.is_added