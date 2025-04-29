#List is mutable(change kr sakhty)[],indexing no.hota 
# l=[1,2,3,4,5]
# print(type(l))
# print(l[4])
# l=[1,2,3,[4,5,6]]
# print(l[3][2])

# l=[2,3,"Hello",[4,5,6]]
# print(l[0:])
# print(l[2::3])#inverse
# print(l[-1::-1])#reversing

#list iteration:
# l=[10,20,30,40,50,60,70,80,90]#inverse
# t=len(l)
# for a in range(t):
#     print(l[a])

# for a in range(t-1,-1,-1): #reverse
#     print(l[a])


#List Comprehension:
# l=[]
# for a in range(1,20):
#     l.append(a)
# print(l)

# n=[h for h in range(1,30) if h%2==0 ]
# print(n)

#append
# l=[2,3,4,5,6]
# w=[8,9,0]
# l.append(w)
# print(l)

# # extend
# l=[2,3,4,5,6]
# w=[8,9,0]
# l.extend(w)
# print(l)

#List Function
#count(),max(),min(),sort(),reverse(),inverse()
l=[1,2,3,4,3,5,6]
# a=l.count(3)
# print(a)

# m=max(l)
# print(m)

# m=min(l)
# print(m)

# l.sort()#sort mean arrangement
# print(l)

# l.reverse()
# print(l)

# o=l.index(6) #indexing
# print(o)

#range
# w=[1,2,3,4,5]
# q=[6,7,8,9]

# t=len(w)
# for h in range(t):
#     print(w[h],q[h])

# abc=["red", "green", "purple"]
# fruits=["Apple", "kiwi", "grapes"]
# for x in abc:
#     for y in fruits:
#         print(x,y)

# def my_func(f1,f2):
#     print(f1+ " "+f2)
# my_func("Summaiya","Imran Bhatti")

# def myfunc(*kids):
#     print("youngest children is:"+ kids[1])
# myfunc("ali", "ahahd","raza","ahsan")

# def myfunc(**kids):
#   print("older student of this years is:" + kids["lastname"])
# myfunc(fname="Ali", lastname="Razan Ali")

# def myfunc(country="Pakistan"):
#     print("My love and my country is "+country)
#     print("I love "+country)
# myfunc("Shoudia Arabia")
# myfunc()

# def myfunc(food):
#     for x in food:
#         print(x)
# fruits=["Apple","Bnana","Kiwi"]
# myfunc(fruits)

# def myfunc(x):
#     return 5*x
# print(myfunc(4))

# def myfunc(n):
#     if n <= 0:
#         print("Hello")
#     else:
#         print(n)
#         myfunc(n-1)
# myfunc(5)

# def countdown(n):
#     if n <= 0:
#         print("Boom!")
#     else:
#         print(n)
#         countdown(n - 1)

#Recursion method:
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)

# class fruits:
#     def __init__(self,name, color, taste):
#         self.name= name
#         self.color= color
#         self.taste= taste
#     def __str__ (self):
#        return f"{self.name}({self.color})({self.taste})" 
# s1=fruits("Apple", "red", "tasty")
# # print(s1.name)
# # print(s1.color)
# # print(s1.taste)
# print(s1)

# class person:
#     def __init__ (self, name, age):
#         self.name= name
#         self.age= age
#     def myfunc(self):
#         print("my name is "+ self.name, " and my age is "+ str(self.age))
# p1=person("summaiya",24)
# p1.myfunc()


# class students:
#     def __init__ (toper,name, age, cgpa):
#         toper.name= name
#         toper.age= age
#         toper.cgpa= cgpa
#     def __str__ (toper):
#         return f"{toper.name}({toper.age})({toper.cgpa})"
# s1=students("Ali",23,3.33)
# print(s1)

# class person:
#     def __init__ (self, fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class student(person):
#     pass
# p1=student("Ali,"," Asad")
# p1.printname()


# class person:
#   def __init__(self,name,lname):
#     self.name=name
#     self.lname=lname
#   def printname(self):
#     print(self.name,self.lname)
  
# class student(person):
#   def __init__(self,name,lname):
#     person. __init__(self,name,lname)

# p1=student("khizar","shahal")
# p1.printname()

#perents to child inheritance:
# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
#     def printname(self):
#         print(self.name,self.age)
# class student(person):
#     def __init__(self,name,age):
#         person.__init__(self,name,age)
# p1=student("Ali",22)
# p1.printname()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printname(self):
#         print(self.name,self.age)
# class student(person):
#     def __init__ (self,name,age):
#             super().__init__(name,age)
# p1=student("HAMDAN YOUSAF",22)
# p1.printname()





















