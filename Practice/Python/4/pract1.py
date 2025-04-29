#Comparison operators
# x=10
# y=20
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)
# print(x<y)
# print(x>y)

#Logical operators
# x=10
# y=20
# print(x!=y and x<y)
# print(x==y or x!=y or x>=y)
# print(x!=y)

#Mutable(list,dict, byte)changes and Immutable(int,char,complex,string,touple,set
# )not changeable data type.
#string data type:
# s='''
#      hello
#         world
# '''
# print(s)
#list
# p=[2.3, "Hello World!", "Summaiya"]
# p[2]=22 changeable
# print(p)

# touple faster then list
# Touple:
# t=(2,3,4.5,"Summaiya")
# print(t, type(t)) is mai list ki tarah hm change data nai kr sakhty

#Dictionary data type(muteable)
# f={"My last day at school":"29 march","My next plan": "Learning to AI"}
# print(f["My last day at school"])
# print(f,type(f))
# print(f["My next plan"])

#Set data type(immutable) remove duplicate value
# d={"My last day at school:29 march","My next plan: Learning to AI"}
# print(d,type(d))

# s={10,20,10,4,67,8,99}#set remove duplicate
# print(s,type(s))

# Type casting using input or int,eval,float:
# p=int(input("Enter the first value:"))
# q=int(input("Enter the second value:"))
# print(p+q)
# v=float(input("Enter the first value:"))
# u=float(input("Enter the second value:"))
# print(v+u)
# s=eval(input("Enter the first value:"))
# r=eval(input("Enter the second value:"))
# print(s+r)

#Conditional operators:
# s=int(input("Enter the number:"))
# if s%3==0:
#     print(s, "odd Number")
# else:
#     print(s, "even number")

#if elif else:
# percentage=int(input("Enter the number:"))
# if percentage>=90:
#     print("First position")
# elif percentage>=80:
#     print("2nd position")
# elif percentage>=70:
#     print("3rd position")
# else:
#     print("Fail")

#Make calculator using if else elif:
# Number1=int(input("Enter the numbers 1:"))

# num1 = int(input("Enter the 1st value:"))
# num2 = int(input("Enter the 2nd value:"))
# print(num1)
# print(num2)

# Number2=int(input("Enter the number 2:"))
# operator=input("Enter the Number:(/,+,-,*):")
# if operator=="+":
#     print(Number1+Number2)
# elif operator=="-":
#     print(Number1-Number2)
# elif operator=="/":
#     print(Number1/Number2)
# elif operator=="*":
#     print(Number1*Number2)
# else:
#     print("NO answer")


def myfunc(name):
    print("My name is: "+name)
myfunc("Sumaiya")

































































