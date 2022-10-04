"""
Parent class representing a person at a university
"""
class UniversityPerson:
    def __init__(self, first_name, last_name, id_number, department) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.department = department
        self.courseList = list()
    
    """
    Parent class function to get the person's name
    """
    def getName(self) -> str:
        return self.first_name + " " + self.last_name
    
    """
    Parent class function to get the person's ID number
    """
    def getIDNum(self) -> int:
        return self.id_number
    
    """
    Parent class function to get the person's department
    """
    def getDepartment(self) -> str:
        return self.department
    
    """
    Abstract parent class function for displaying information. This function is overridden in child classes
    """
    def display() -> None:
        pass

"""
Class to represent a student at a university
"""
class Student(UniversityPerson):
    """
    Class function to enroll into a class
    """
    def enroll(self, className) -> None:
        self.courseList.append(className.upper())
        print("Success: You have enrolled in the class.")
    
    """
    Class function to drop from an enrolled class
    """
    def drop(self, className) -> None:
        if(className.upper() in self.courseList):
            self.courseList.remove(className.upper())
            print("Success: You have dropped that class.")
        else:
            print("Error: You are not currently enrolled for that class.");
    
    """
    (Override) Class function to display all information about this student
    """
    def display(self) -> None:
        print("Student:")
        print("\t", self.getName())
        print("\t", self.getIDNum())
        print("\t", self.getDepartment())
        print("\t", self.courseList)

"""
Class to represent a professor teaching at a university
"""
class Professor(UniversityPerson):    
    """
    Class function to add a class to this professors teaching list
    """
    def add(self, className) -> None:
        self.courseList.append(className.upper())
        print("Success: You are now teaching that class.")
    
    """
    Class function to remove a class from this professors teaching list
    """
    def remove(self, className) -> None:
        if(className.upper() in self.isTeaching):
            self.courseList.remove(className.upper())
            print("Success: You are no longer teaching that class.")
        else:
            print("Error: You cannot remove a course you were not originally teaching.")
    
    """
    (Override) Class function to display all information about this student
    """
    def display(self) -> None:
        print("Employee:")
        print("\t", self.getName())
        print("\t", self.getIDNum())
        print("\t", self.getDepartment())
        print("\t", self.courseList)

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