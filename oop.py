from distributed.utils_test import double


class Person:
    def __init__(self, name):
        self.__name = str(name)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def display(self):
        print("name : ", self.__name)


class Employee(Person):

    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.__salary = salary

    def setSalary(self, salary):
        self.__salary = double(salary)

    def getSalary(self):
        return self.__salary

    def display(self):
        print("salary : ", self.getSalary())
        Person.display(self)


class Add:
    __firstNumber = 0
    __secondNumber = 0

    def __init__(self, fNum, sNum):
        self.secondNumber = int(sNum)
        self.firstNumber = int(fNum)

    def getFirstNumber(self):
        return self.firstNumber

    def getSecondNumber(self):
        return self.secondNumber

    def getResult(self):
        result = self.getFirstNumber() + self.getSecondNumber()
        return result

    def printResult(self):
        print("result = ", self.getResult())


# # to declare an object and use its methods
# per = Person()
# name = input("Enter your name : ")
# per.setName(name)
# per.printName()

# add = Add(input("Enter first number : "), input("Enter second number : "))
# add.printResult()

emp = Employee(input("Enter your name : "), input("Enter your salary : "))
emp.display()
