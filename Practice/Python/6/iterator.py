#iterator 
# this_iterator=("Apple","Banana","Mango")
# my_iterator=iter(this_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# for x in this_iterator:
#     print(x)
# 
#string in iterator:
# mystr= "Apple"
# for x in mystr:
#     print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass = MyNumbers()
# iter=iter(myclass)
# print(next(iter))

#Stop iterator mai yeh code likha jata hai:
# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a <=20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
# myclass=MyNumbers()
# iterate=iter(myclass)
# for x in iterate:
#     print(x)

#Polymorphism:
# class cars:
#     def move(self):
#         print("Honda Civix")
# class boats:
#     def move(self):
#         print("Especilly boats")
# for x in cars(), boats():
#     x.move()

# class vehicle:
#     def move(self):
#         print("moves")
# class car(vehicle):
#     pass
# class boat(vehicle):
#     def move(self):
#         print("no")
# for a in (car(),boat()):
#     a.move()

# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# x=person("Ali","Asghar")
# x.printname()

# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class student(person):
#         def __init__(self, fname, lname,year):
#              super().__init__(fname, lname)
#              self.graduationyear= year 
#         def show(self):
#              print(f"{self.fname} {self.lname} {self.graduationyear}")
# x=student("Summaiya", "Gull", 2025)
# x.show()

# class person:
#     def __init__ (self,fname, lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class student(person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname)
#         self.graduation=year
#     def welcome(self):
#         print(f"Welcome to new student" , self.fname,self.lname,"in the year of", self.graduation)
# x=student("Summaiya","Zafar",2025)
# x.welcome()

#Iterator:
# x=("Apple","Banana","Grapes")
# myiter=iter(x)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))       

# x="banana"
# for a in x:
#     print(a)
# mystr=iter(x)
# print(next(mystr))
# print(next(mystr))
# print(next(mystr))
# print(next(mystr))
# print(next(mystr))
# print(next(mystr))

# x=("Apple","Banana","Grapes")
# for a in x:
#     print(a)

# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printname(self):
#         print(self.name,self.age)
# class students(parent):
#         def __init__(self, name, age,degree):
#              super().__init__(name, age)
#              self.degree=degree
#         def show(self):
#              print(f"hello",self.name, "your age is",self.age,"and your degree plan is ", self.degree)
# myclass=students("Ali",22,"BSIT")
# myclass.show()

#polymorphism:
# class car:
#     def __init__(self, name, model):
#         self.name=name
#         self.model=model
#     def move(self):
#         print("drive")
# class boat:
#     def __init__(self,name, model):
#         self.name=name
#         self.model=model
#     def move(self):
#         print("Snail")
# class plane:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     def move(self):
#         print("butter")
# car1=car("honda", 2020)
# boat1=boat("basid",2002)
# plane1=plane("PIA",1998)
# for x in (car1,boat1,plane1):
#     x.move()

# def myfunc():
#     x=300
#     def another():
#         print(x)
#     another()
# myfunc()

# x=40   global variables under or bahir dono jgha call ho jata hai
# def myfunc():
#     print(x)
# myfunc()
# print(x)

# local or global variable:pehly under or phir bahir call hota hai
# x=30
# def myfunc():
#     x=40
#     print(x)
# myfunc()
# print(x)

# global as a keyword;
# def myfunc():
#     global x
#     x=30
# myfunc()
# print(x)

# x=300 #bahir wali value ko ignore kr kai under wali ko return kry ga
# def myfunc():
#     global x
#     x=200
# myfunc()
# print(x)

#ik func ko ignore kr kai dosry waly ki value print krwana
# def myfunc():
#     x="Summaiya"
#     def thisfunc():
#         nonlocal x
#         x="Gull"
#     thisfunc()
#     return x
# print(myfunc())

#Module:
def greeting(name):
    print("Hello, "+ name)
import mymodule

mymodule.greeting("Jonathan")













    












































