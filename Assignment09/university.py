"""
Class to represent a student at a university
"""
class Student:
    def __init__(self, first_name, last_name, student_id, major_of_study) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major_of_study = major_of_study
        self.isTaking = list()
    
    """
    Class function to get the full name of a Student
    """
    def getName(self) -> str:
        return self.first_name + " " + self.last_name
    
    """
    Class function to get the id of the student
    """
    def getStudentID(self) -> int:
        return self.student_id
    
    """
    Class function to get the major of study for this student
    """
    def getMajor(self) -> str:
        return self.major_of_study
    
    """
    Class function to enroll into a class
    """
    def enroll(self, className) -> None:
        self.isTaking.append(className.upper())
        print("Success: You have enrolled in the class.")
    
    """
    Class function to drop from an enrolled class
    """
    def drop(self, className) -> None:
        if(className.upper() in self.isTaking):
            self.isTaking.remove(className.upper())
            print("Success: You have dropped that class.")
        else:
            print("Error: You are not currently enrolled for that class.");
    
    """
    Class function to display all information about this student
    """
    def display(self) -> None:
        print("Student:")
        print("\t", self.getName())
        print("\t", self.getStudentID())
        print("\t", self.getMajor())
        print("\t", self.isTaking)

"""
Class to represent a professor teaching at a university
"""
class Professor:
    def __init__(self, first_name, last_name, employee_id, department) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department
        self.isTeaching = list()

    """
    Class function to get the full name of a Student
    """
    def getName(self) -> str:
        return self.first_name + " " + self.last_name
    
    """
    Class function to get the employee id
    """
    def getEmployeeID(self) -> int:
        return self.employee_id
    
    """
    Class function to get the department they are working for
    """
    def getDepartment(self) -> str:
        return self.department
    
    """
    Class function to add a class to this professors teaching list
    """
    def add(self, className) -> None:
        self.isTeaching.append(className.upper())
        print("Success: You are now teaching that class.")
    
    """
    Class function to remove a class from this professors teaching list
    """
    def remove(self, className) -> None:
        if(className.upper() in self.isTeaching):
            self.isTeaching.remove(className.upper())
            print("Success: You are no longer teaching that class.")
        else:
            print("Error: You cannot remove a course you were not originally teaching.")
    
    """
    Class function to display all information about this student
    """
    def display(self) -> None:
        print("Employee:")
        print("\t", self.getName())
        print("\t", self.getEmployeeID())
        print("\t", self.getDepartment())
        print("\t", self.isTeaching)

##################################################
msmith = Professor("Michael", "Smith", 1112577, "Computer Science")
abarber = Professor("Andrew", "Barber", 1122557, "Mathematics")
jsmith = Student("John", "Smith", 1223456, "Computer Science")
tmateo = Student("Tina", "Mateo", 1233455, "Mathematics")

msmith.add("ICSI201")
msmith.add("ICSI213")
msmith.add("ICSI499")

abarber.add("AMAT113")
abarber.add("AMAT214")
abarber.add("AMAT311")

jsmith.enroll("ICSI201")
jsmith.enroll("AMAT113")

tmateo.enroll("AMAT113")

print("\n\n")
msmith.display()
print()
abarber.display()
print()
jsmith.display()
print()
tmateo.display()