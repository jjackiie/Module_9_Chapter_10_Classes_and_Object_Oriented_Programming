# ====================================
# Attached: m11 Homework #11
# ====================================
# File: Project #1
# ====================================
# Name: Pet Class
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# start the Pet function
class Pet:
    # here we have three arguments
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age

    # this assigns a value to the __name field
    def set_name(self, name):
        self.__name = name

    # this returns the value of the __name field
    def get_name(self):
        return self.__name

    # this assigns a value to the __type field
    def set_type(self, type):
        self.__type = type

    # this returns the value of the __type field
    def get_type(self):
        return self.__type

    # this assigns a value to the __age field
    def set_age(self, age):
        self.__age = age

    # this returns the value of the __age field
    def get_age(self):
        return self.__age


# the main function
def main():

    # asking the user the following questions
    name = input("What is the name of the pet? ")
    type = input("What type of pet? ")
    age = int(input("How old is your pet? "))

    # creating an object from th Pet class
    pets = Pet(name, type, age)

    # formatting and displaying the following using the object's accessor method/
    print("The pet's name: ", pets.get_name)
    print("The animal type: ", pets.get_type)
    print("The pet's age: ", pets.get_age)


# calling the main function
main()


''''
=================== Output ===========================


'''


# ====================================
# Attached: m11 Homework #11
# ====================================
# File: Project #2
# ====================================
# Name: Employee Class
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# start the Employee function
class Employee:
    # this assigns a value to the different fields
    def __init__(self):
        self.name = None
        self.id = None
        self.department = None
        self.job_title = None

    # it is used to access variables that belong to that class
    def GetInformation(self):
        print("----Name----" + "----ID Number----" + "----Department----" + "----Job Title----")
        print(self.name + self.id + self.department + self.job_title)

# creates the Employee 1 object
employee1 = Employee()
employee1.name = "Susan Meyers"
employee1.id = "47899"
employee1.department = "Accounting"
employee1.job_title = "Vice President"


# creates the Employee 2 object
employee2 = Employee()
employee2.name = "Mark Jones"
employee2.id = "39119"
employee2.department = "IT"
employee2.job_title = "Programmer"

# creates the Employee 3 object
employee3 = Employee()
employee3.name = "Joy Rogers"
employee3.id = "81774"
employee3.department = "Manufacturing"
employee3.job_title = "Engineer"


# calling the function
employee1.GetInformation()
employee2.GetInformation()
employee3.GetInformation()


''''
=================== Output ===========================


'''

# ====================================
# Attached: m11 Homework #11
# ====================================
# File: Project #3
# ====================================
# Name: Retail Item Class
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class RetailItem:
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

item1 = RetailItem()
item1.description = "Jacker"
item1.units = "12"
item1.price = "$59.95"

item2 = RetailItem("Designer Jeans", "40", "$34.95")

item3 = RetailItem()
item3.description = "Shirt"
item3.units = "40"
item3.price = "$24.95"






''''
=================== Output ===========================



'''