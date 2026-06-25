name = 10#same for negative and positive number
name1 = 10
print(name==name1)# avlue
print(name is name1)#value address
print(id(name1))
# is ->in a given address (-5 to 256)

#CONDITIONAL STATEMENT
#if
num=10
num2=20
if num<num2:
    print(num2)

#if else
num1=int(input("enter the number"))
if num1:
    print("number",num1)
else:
    print("zero",num1)

#if elif
age=int(input("enter your age"))
if age==18:
    print("your age is",age)
elif age>18:
    print("you are adult")
else:
    print("you are not adult")

question

marks=int(input("enter your marks"))
if marks<60:
    print("you failed")
elif 60<marks<74:
    print("you got C grade")
elif 75<marks<90:
    print("you got B grade")   
else:
    print("you got A grade") 

loops

for i in range(5):
    print("i=",i)

#lists

l=[11,12,13,14,15,16]
print(len(l))
for i in range(4):
    print(l[i])

#list example
l=[10,[11,12,13,14,15]]
for i in l[1]:
    print(i)

print("second approach")
for i in range(len(l[1])):
    print(l[1][i])

    #break 
    for i in range(5):
        if i == 2:
            break
        print(i)

#contionue
i=0 
while true:
    if i == 5 :
      break
    else :
        i+=1
        continue

    # pass bypass ka kaam aata h koi error aaye toh

