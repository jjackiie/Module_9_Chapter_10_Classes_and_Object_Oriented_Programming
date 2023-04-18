# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #1
# ====================================
# Name: Students Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Students:
    # the keyword (self)
    # it is used to access variables that belong to that class
    def GetInformation(self):
        print("The student's last name is " + self.Lastname)
        print("The student's first name is " + self.Firstname)
        print("The student's address name is " + self.Address)
        print("The student's city name is " + self.City)
        print("The student's state name is" + self.State)
        print("The student's zipcode name is " + self.Zipcode)

        # creates the Student1 object
        student1 = Students()
        student1.Lastname = "Doe"
        student1.Firstname = "Jane"
        student1.Address = "111 St"
        student1.City = "Santa Ana"
        student1.State = "CA"
        student1.Zipcode = "12345\n"

        # creates the Student2 object
        student2 = Students()
        student2.Lastname = "Cantor"
        student2.Firstname = "Mike"
        student2.Address = "222 St"
        student2.City = "Garden Grove"
        student2.State = "CA"
        student2.Zipcode = "67890\n"

        # creates the Student3 object where the user will be able to enter the student's information
        student3 = Students()
        student3.Lastname = input("What is the Student 3's last name? ")
        student3.Firstname = input("What is the Student 3's first name? ")
        student3.Address = input("What is the Student 3's address? ")
        student3.City = input("What is the Student 3's city? ")
        student3.State = input("What is the Student 3's state? ")
        student3.Zipcode = input("What is the Student 3's zipcode? ")

        # calling the function
        student1.GetInformation()
        student2.GetInformation()
        student3.GetInformation()



''''
=================== Output ===========================


'''