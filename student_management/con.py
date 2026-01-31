class student:
    def __init__(self, name, dateOfBirth, examMark):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark
        self.__fullTimeStudent = True

    def displayExamMark(self):
        return(self.__examMark)

    def displayInfo(self):
        if self.__fullTimeStudent:
            self.__x = "FullTime"
        else:
            self.__x = "PartTime"
        return(self.__name, self.__dateOfBirth, self.__examMark, self.__x)

class fullTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        super().__init__(name, dateOfBirth, examMark)
        self._student__fullTimeStudent = True # Note: Name mangling workaround if needed, but the original code had a flaw in how it set the private variable of the parent class.

# Fixed version to actually work as intended:
class Student:
    def __init__(self, name, dateOfBirth, examMark):
        self._name = name
        self._dateOfBirth = dateOfBirth
        self._examMark = examMark
        self._fullTimeStudent = True

    def displayExamMark(self):
        return self._examMark

    def displayInfo(self):
        student_type = "FullTime" if self._fullTimeStudent else "PartTime"
        return (self._name, self._dateOfBirth, self._examMark, student_type)

class FullTimeStudent(Student):
    def __init__(self, name, dateOfBirth, examMark):
        super().__init__(name, dateOfBirth, examMark)
        self._fullTimeStudent = True

class PartTimeStudent(Student):
    def __init__(self, name, dateOfBirth, examMark):
        super().__init__(name, dateOfBirth, examMark)
        self._fullTimeStudent = False

def run_student_demo():
    print("--- Student Management ---")
    fullstudent = FullTimeStudent("Merka Jojka", "6/6/2666", 64)
    partstudent = PartTimeStudent("Tester Makester", "12/12/3666", 101)
    print(f"Full-time student exam mark: {fullstudent.displayExamMark()}")
    print(f"Part-time student exam mark: {partstudent.displayExamMark()}")
    print(f"Full-time student info: {fullstudent.displayInfo()}")
    print(f"Part-time student info: {partstudent.displayInfo()}")

if __name__ == "__main__":
    run_student_demo()
