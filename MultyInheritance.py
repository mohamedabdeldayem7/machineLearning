class Father:
    def __init__(self, fatherName):
        self.__fatherName = fatherName

    def display(self):
        print("father name : ", self.__fatherName)


class Mother:
    def __init__(self, motherName):
        self.__motherName = motherName

    def display(self):
        print("mother name : ", self.__motherName)


class Son(Father, Mother):
    def __init__(self, name, fatherName, motherName):
        Father.__init__(self, fatherName)
        Mother.__init__(self, motherName)
        self.__name = name

    def display(self):
        Father.display(self)
        Mother.display(self)
        print("son name : ", self.__name)


son = Son("mohamed", "father", "mother")
son.display()
