class Person:
    def __init__(self,fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'fullname: {self.fullname}, age: {self.age}, is_married: {self.is_married}'



class Student:
    def __init__(self, fullname, age, is_married,marks):
        super().__init__(Person)
        self.marks = marks

Mike=Person('Mike',3,True)
print(Mike.introduce_myself())