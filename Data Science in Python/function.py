# Functions is a block of code which only rum when we called. 
#you can pass data, known as parameter , into a function.
#function can return data as a result.
#in python, a function  is defined using def keyword.
# def greet_user():
#     print("Hello! Dear Summaiya")
# greet_user()

# def user(name):
#     print(f"Asslam o Alaekum! {name}, Kaifa Haluk")
# user("Summaiya")


# def user_name(name="Dear bro"):
#     print(f"Asslam o Alaekum {name} ! Kaifa Haluk?")
# user_name("Ehsan")

# def square(number):
#     return number*number
# print(square(8+3))

# def square(number):
#     return number*number
# result=square(8)
# print(result)

# #Recursion:
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(4))


#Lamda function: 10 example khud likhni hai using define + simple lambda 
def x(a,b):
    return a/b
x= lambda a, b : a*a/b
print(x(6,3))