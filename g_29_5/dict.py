# # Basic dictionary in Python

# # Creating a dictionary
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

# # Accessing values
# print(student["name"])
# print(student["age"])

# # Adding a new key-value pair
# student["city"] = "Jaipur"

# # Updating a value
# student["age"] = 21

# # Printing the whole dictionary
# print(student)

# # Looping through dictionary
# for key, value in student.items():
#     print(key, ":", value)


    
# d={"adddress":{"adddress1":{"city":"kukas","districr":"jaipur"},
#  "adddress2":{"city":"gopalpura","district":"arya mains"}}}

# print(d)
# print(d["adddress"])
# for key, value in d.items():
#     print(key, ":", value)

# d={"address":{"address1":{"city":"kukas","district":"jaipur"},
#                "address2":{"city":"gopalpura","district":"arya mains"}}}
# print(d["address"])
# print(d["address"]["address1"])
# print(d["address"]["address1"]["city"])


#nested dictionary


# Basic example of a nested dictionary

# students = {
#     "student1": {
#         "name": "Rahul",
#         "age": 20,
#         "marks": 85
#     },
    
#     "student2": {
#         "name": "Priya",
#         "age": 22,
#         "marks": 90
#     }
# }

# # Accessing nested dictionary values
# print(students["student1"]["name"])
# print(students["student2"]["marks"])

# # Printing all data
# for student, details in students.items():
#     print(student)
#     for key, value in details.items():
#         print(key, ":", value)


        #nested lists


# Basic example of a nested list

# students = [
#     ["Rahul", 20, 85],
#     ["Priya", 22, 90],
#     ["Aman", 21, 88]
# ]

# # Accessing elements
# print(students[0][0])   # Rahul
# print(students[1][2])   # 90

# # Looping through nested list
# for student in students:
#     print("Name:", student[0])
#     print("Age:", student[1])
#     print("Marks:", student[2])
#     print()


    #map transform values ,fiter select values, reduces combine values
# inme km se km 2 argument pass krne honge

# def square(x):
#     return x*x
# #map
# l=[10,20,30]
# l1=list(map(square,l))
# print(l1)



# map() → Applies a function to every item in a sequence.
# filter() → Selects items from a sequence based on a condition.
# reduce() → Reduces a sequence to a single value by repeatedly applying a function.

# from functools import reduce

# # List of numbers
# numbers = [1, 2, 3, 4, 5, 6]

# # map() -> square each number
# squares = list(map(lambda x: x**2, numbers))
# print("Squares:", squares)

# # filter() -> keep only even squares
# even_squares = list(filter(lambda x: x % 2 == 0, squares))
# print("Even Squares:", even_squares)

# # reduce() -> add all even squares
# total = reduce(lambda x, y: x + y, even_squares)
# print("Sum of Even Squares:", total)



# l=["apple","banana","cat","dog"]
# upper_words = list(map(str.upper, l))

# print(upper_words)


# try except finally

try:
    number1=int(input("enter the first num"))
    number2=int(input("enter the second num"))
    print(number1/number2)

except:
    print("error ")    


finally:
    print("program executed")