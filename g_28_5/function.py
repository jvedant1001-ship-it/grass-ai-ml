# # def -> declaration 
# # argument -> 
# # parameter -> 
# # def hello():
# #     print("hello function is working")
   
# # hello()

# #example 2

# def hello1(a):
#     print(a)

# hello1(100)

# def add(a=22,b=33):# defaukt value
#     print(a+b)

# add(10,5)

# def power(a,b):
#     print(a**b)

# power(2,5)
# power(5,2)
# power(b=5,a=2)


# def address(a):
#     for i in a:
#         for j in i :
#             print(j)

# address(["hello","world"])


# def sum(a,b):
#     return a+b

# result=sum(10,20)
# print(result)

#  LAMBDA FUNCTION pdhna ek baar imp h

# add= lambda x:x
# print(add(100))


# sum = lambda x,y:x+y
# print(sum(10,20))

# add = lambda *numbers: sum(numbers)

# print(add(1, 2, 3))
# print(add(10, 20, 30, 40))


#list comphresion  single line n loop

# l=[10,20,30,40,50]
# print(l[i] for i in range(len(l)))


#list mutable hoti h
# l=[10,20,30,40,50,"hello","true"]
# print(l)
# print(l[0])
# print(l[-1])
# print(l[-2])

# l.append("new")
# print(l)

# l.insert(1,100)
# print(l)

# #question
# l=[10,20,30,{"name":"yourname","address":["jaipour","kukas","hometown"]}]
# print(l[3])
# print(l[3]['address'])

l=[10,20,30,[40,50,[60,70,80]]]
print(l[3][0])
