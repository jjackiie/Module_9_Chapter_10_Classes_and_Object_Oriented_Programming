# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #1
# ====================================
# Name: Students' Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# start the Students function
class Students:
    # the keyword (self)
    # it is used to access variables that belong to that class
    def GetInformation(self):
        print("The student's last name is " + self.Lastname)
        print("The student's first name is " + self.Firstname)
        print("The student's address name is " + self.Address)
        print("The student's city name is " + self.City)
        print("The student's state name is " + self.State)
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
What is the Student 3's last name? Gomez
What is the Student 3's first name? Josh
What is the Student 3's address? 12345
What is the Student 3's city? Orange
What is the Student 3's state? CA
What is the Student 3's zipcode? 456789

The student's last name is Doe
The student's first name is Jane
The student's address name is 111 St
The student's city name is Santa Ana
The student's state name is CA
The student's zipcode name is 12345

The student's last name is Cantor
The student's first name is Mike
The student's address name is 222 St
The student's city name is Garden Grove
The student's state name is CA
The student's zipcode name is 67890

The student's last name is Gomez
The student's first name is Josh
The student's address name is 12345
The student's city name is Orange
The student's state name is CA
The student's zipcode name is 456789

'''


# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #2
# ====================================
# Name: Teachers' Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# start the Teacher function
class Teacher:
    # using init to create a customized constructor
    # here we have three arguments
        def __init__(self, name, classRoom, course):
            self.name = name
            self.classRoom = classRoom
            self.course = course

        # formatting the outcome with the three arguments
        def GetProfessor(self):
            print("The professor's name is " + self.name)
            print("The professor's assigned class is " + self.classRoom)
            print("The professor is teaching " + self.course)

# assigning the variables with the outcomes
Teacher1 = Teacher("Professor Sim", "A106", "Python Programming \n")
Teacher2 = Teacher("Professor Tak", "A206", "C++ Programming")

# calling the arguments
Teacher1.GetProfessor()
Teacher2.GetProfessor()

''''
=================== Output ===========================
The professor's name is Professor Sim
The professor's assigned class is A106
The professor is teaching Python Programming

The professor's name is Professor Tak
The professor's assigned class is A206
The professor is teaching C++ Programming

'''


# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #3
# ====================================
# Name: Passing Parameters
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# start the PI function
class PI:

    # passing the 7 parameters
    def GetInformation(self, LN, FN, Age, Address, City, State, Zipcode):
        return LN + " , " + FN + " , " + str(Age) + " , " + Address + " , " + City + " , " + State + " , " + Zipcode

# assigning the class to the variable
PersonalInformation = PI()

# assigning the variables and asking the user the following statements
PersonalInformation.Lastname = input("Enter the last name: ")
PersonalInformation.Firstname = input("Enter the first name: ")
PersonalInformation.Age = int(input("Enter the age: "))
PersonalInformation.Address = input("Enter the address: ")
PersonalInformation.City = input("Enter the city: ")
PersonalInformation.State = input("Enter the state: ")
PersonalInformation.Zipcode = input("Enter the zipcode: ")

# displaying and formatting the outcome
print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname,
                                         PersonalInformation.Age, PersonalInformation.Address,
                                         PersonalInformation.City, PersonalInformation.State,
                                         PersonalInformation.Zipcode))

''''
=================== Output ===========================
Enter the last name: Bond
Enter the first name: James
Enter the age: 55
Enter the address: 123 Circle St
Enter the city: Orange
Enter the state: CA
Enter the zipcode: 12345
Bond , James , 55 , 123 Circle St , Orange , CA , 12345


'''


# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #4
# ====================================
# Name: Class 7
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# import the other class file name
import class7

# start the main function
def main():
    # assigning the variables while asking the user to enter the following info
    name = (input("Enter the name: "))
    age = (input("Enter the age: "))
    address = (input("Enter the address: "))
    phone = (input("Enter the phone: "))
    city = (input("Enter the city: "))
    zipcode = (input("Enter the zipcode:  "))

    # calling class7 or the first file, then the name of the class, then the name of the function which equals to the input variables
    v1 = class7.customer.set_name = name
    v2 = class7.customer.set_age = age
    v3 = class7.customer.set_address = address
    v4 = class7.customer.set_phone = phone
    v5 = class7.customer.set_city = city
    v6 = class7.customer.set_zipcode = zipcode

    # displaying and formatting the info
    print("Hello " + v1 + ", your age is " + v2 +
          ", your address is " + v3 + ", your phone number is "
          + v4 + ", your city is " + v5 + ", and the zipcode is " + v6)

# calling the main function
main()

''''
=================== Output ===========================
Enter the name: William
Enter the age: 19
Enter the address: 123 Prince Ave
Enter the phone: 1213456789
Enter the city: Bel Air
Enter the zipcode:  92834
Hello William your age is 19, your address is 123 Prince Ave, your phone number is 1213456789, your city is Bel Air, and the zipcode is 92834

'''

# ====================================
# Attached: m11 Class Exercise #9
# ====================================
# File: Challenge Exercise #5
# ====================================
# Name: Class 3
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# import the other class file name
import class3

# start the main function
def main():

    # asking the user the starting balance
    start_bal = float(input("Enter the starting balance: "))

    # call the external class3.name of the class which in our case its class BankAccount from the class 3
    saving = class3. BankAccount(start_bal)

    # assigning a variable and asking the user how much they were paid this week
    pay = float(input("How much were you paid this week? "))
    # displaying a sentence that ensures the user that their money will be deposited
    print("Will deposit that amount into your account. \n")

    # the deposit function is passing one argument called amount, so we have to fulfill the argument with pay
    saving.deposit(pay)

    # retrieved the balance from the external class
    print("Your account balance is $", format(saving.get_balance(), ",.2f \n"))

    # assigning a variable and asking the user how much they would like to withdraw
    cash = float(input("How much would you like to to withdraw? "))
    # displaying a sentence that ensures the user that withdrawal will be taken into account
    print("Will withdraw that amount from your account. \n")

    # calls the withdrawal function from the external class and fulfills the one argument that is passed with cash
    saving.withdraw(cash)

    # retrieved the balance from the external class
    print("Your account balance is $", format(saving.get_balance(), ",.2f"))

# calling the main function
main()

''''
=================== Output ===========================
Enter the starting balance: 4
How much were you paid this week? 5000000
Will deposit that amount into your account.

Your account balance is $ 5,000,004.00

How much would you like to to withdraw? 20000
Will withdraw that amount from your account.

Your account balance is $ 4,980,004.00

Process finished with exit code 0


'''