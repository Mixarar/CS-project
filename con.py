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
        return(self.__name,self.__dateOfBirth,self.__examMark, self.__x)

class fullTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        super().__init__(name, dateOfBirth, examMark)
        self.__fullTimeStudent = True

class partTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        super().__init__(name, dateOfBirth, examMark)
        self.__fullTimeStudent = False


fullstudent = fullTimeStudent("Merka Jojka", "6/6/2666", 64)
partstudent = partTimeStudent("Tester Makester", "12/12/3666", 101)
print(fullstudent.displayExamMark())
print(partstudent.displayExamMark())
print(fullstudent.displayInfo())
print(partstudent.displayInfo())