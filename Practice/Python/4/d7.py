#what is list function in python:
# l=[10,20,30,40,50,60,60,60,60]
# c=l.count(60)
# d=max(l)
# e=min(l)
# print(c)
# print(d)
# print(e)

# d=["Summaiya","deeply"]
# m=max(d)
# print(m)
#Sort mean arrangement: ascendind order
# d=[2,4,7,6,4,5,6,8,9,1,5]
# d.sort()
# print(d)
# #Reverse function:
# d.reverse()
# print(d)
# a=d.index(7)
# print(a)

# l=[20,30,40,50,60]
# l1=[20,30,40,50,60,70]
# for a,b in zip(l,l1):
#     print(a,b)
# t=len(l)
# for a in range(t):
#     print(l[a],l1[a])

#Convert string to list in python program:
# p=input("Enter the value: ")#list mai elements alagh alagh split ho jaty hai
# n=p.split()
# print(n)
# n=[]
# for a in range(1,5):
#     k=input("Enter the value "+str(a)+":")
#     n.append(k)
# print(n)
#Once more example:
# v=[]
# for s in range(1,3):
#     o=input("Enter the names "+str(s)+":")
#     v.append(o)
# print(v)

#Sort list
# thislist=["Banana", "Cherry", "Mango", "Apple"]
# thislist.sort(reverse=True)
# print(thislist)
# thislist.sort()
# print(thislist)

# def myfunc(m):
#     return abs(m-40)
# list=[20,40,30,60,10,70]
# list.sort(key=myfunc)
# print(list)
#case insensitive list
# mylist=["apple", "Orange", "Kiwi", "cherry"]
# mylist.sort()
# mylist.insert(1, "orange")
# print(mylist)
# mylist.sort(key= str.lower)
# print(mylist)
# thislist=mylist[:]#copy kai liyee 2 tarah sy hm likh sakhty hai ik colon kai sath or ik thislist=mylist.copy() essy b likh sakhty 
# print(thislist)

#List concatnate:
# list1=[1,2,3,4]#method 1
# list2=["a","b","c","d"]
# list3=list1+list2
# print(list3)
# for x in list2: #method 2
#     list1.append(x)
# print(list1)
# list1.extend(list2)#method 3
# print(list1)

# mylist=("apple",)
# print(mylist)
# print(type(mylist))
# print(len(mylist))
#change touple:
# x=("apple", "orange", "banana", "cherry")
# y=list(x)
# y[2]="kiwi"
# x=list(y)
# print(x)

#append in tuple:
# mylist=("apple", "orange", "banana", "cherry")
# y=list(mylist)
# y.append("orange")
# mylist=tuple(y)
# print(mylist)

# Python - Unpack Tuples
# mylist=("apple", "orange", "banana", "cherry")
# y=("Apple" ,)#append krna mtlb last mai ik value add krna
# thislist += y
# print(thislist)

# remove in tuple
# mylist=("apple", "orange", "banana", "cherry")
# y=list(mylist)
# y.remove("apple")
# mylist=tuple(y)
# print(mylist)

# multiple_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, red, *pink) = multiple_fruits
# print(green)
# print(red)
# print(pink)
#Count method in tuple:
# multiple_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry","apple")
# fruits=multiple_fruits.count("apple")
# print(fruits)

#index method in tuple:
# multiple_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# fruits=multiple_fruits.index("apple")
# print(fruits)

# myset = {"apple", "banana", "cherry"}
# for a in myset:
#     print(a)

#set mai change or duplicate nai hita but add or update ho jata hai:
# myset = {"apple", "banana", "cherry", "grapes","mango"}
# thisset={"kiwi","mango","respberry", "apple"}
# thisset.update(myset)#update method
# print(thisset)

# myset.add("orange")#add method
# print(myset)

#method of set(remove, discard, clear, delete, pop)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.remove("apple")
# print(x)
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.discard('banana')
# print(x)
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.clear()
# print(x)
# print(thisset)
# myset = {"apple", "banana", "cherry"}
# del myset
# print(myset)set1 = {"a", "b", "c"}

#set mai combine or join mai yeh method hoty hai(union, update, intersection, difference, symmetric_difference) 
# list1={"Summaiya", "Sadiqa","Ruqia", "Mubashreen", "Hajira"}
# list2={"Ehsan", "Musarat", "Ami jaan", "Abu g"}
# list3=list1.union(list2)
# print(list3)

# list1={"Summaiya", "Sadiqa","Ruqia", "Mubashreen", "Hajira"}
# list2={"Ehsan", "Musarat", "Ami jaan", "Abu g"}
# list1.update(list2)
# print(list1)

# list1={"Summaiya", "Sadiqa","Ruqia", "Mubashreen", "Hajira"}
# list2={"Ehsan", "Musarat", "Ami jaan", "Abu g"}
# list1.intersection(list2)
# print(list1)

# list1={"Summaiya", "Sadiqa","Ruqia", "Mubashreen", "Hajira"}
# list2={"Ehsan", "Musarat", "Ami jaan", "Abu g"}
# list1.difference(list2)
# print(list1)

# list1={"Summaiya", "Sadiqa","Ruqia", "Mubashreen", "Hajira"}
# list2={"Ehsan", "Musarat", "Ami jaan", "Abu g"}
# list1.symmetric_difference(list2)
# print(list1)






































































































