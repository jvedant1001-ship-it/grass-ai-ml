class vedant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getage(self):
        print("my age is", self.age)

    def getname(self):
        print("my name is", self.name)

v = vedant("hello", 20)
v.getage()
v.getname()