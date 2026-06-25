#inheritance


class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state 

    def location(self):
        return f"my location is {self.city} in {self.state}"


class user(address):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def username(self):
        print(f"my name is {self.name} and age is {self.age}")    

u = user("vedant",20)
u.username()
a=address("kukas","rajasthan")
print(a.location())




#encapsulation

class address:
    def __init__(self,city,state):
         self.city=city
         self.state=state
    def location(self):
        print(f"my location is {self.city} in {self.state}")    


a=address("chhapra","bihar")
a.location()
print(a.state)
print(a.city)


# polymorphism

class address:
    def __init__(self,city,state):
         self.city=city
         self.state=state
    def location(self):
        print(f"my location is {self.city} in {self.state}")    

class hometown:
    def __init__(self,city,state):
          self.city=city
          self.state=state

    def location(self):
        print(f"my location is {self.city} in {self.state}")    


a=address("vadodra","gujrat")        
a.location()
b=hometown("chappra","bohea")
b.location()




class address:
    def __init__(self,city,state):
         self.city=city
         self.state=state
    def location(self):
        print("location")

a=address("jaipur","rajasthan")
a.location()



# method overloading 
class Calculator:
    def add(self, a, b=0):
        return a + b

c = Calculator()

print(c.add(5))      # 5
print(c.add(5, 3))   # 8


# method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
d = Dog()

a.sound()  # Animal makes a sound
d.sound()  # Dog barks


# tuples 
fruits = ("apple", "banana", "mango")

print(fruits)