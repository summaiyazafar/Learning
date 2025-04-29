#for Loop using range:start=1,condition>6,increment:2:-
# for a in range(1,30,5):
    # print("My first day")
# for n in range(1,11):
    # print("2*",n,"=",2*n) inverse

# x="Bscs"
# def myfunc():
#     x="Summaiya"
#     print("My name is:" + x)
# myfunc()
# print("my study plan is:" + x)

# c="plan"
# def myfunc():
#     global c
#     print("my new:" + c)

# age=24
# myname=f"My name is Summaiya and I am {age} years old."
# print(myname)
# def myfunc():
#     return True
# if myfunc():
#     print("Yes")
# else:
#     print("No")

# l=["Sundas", "Ali", "Samaila","sundila","Adan"]
# # print(l[2:5])
# # print(len(l))
# l[2]=3
# print(l)
# print(len(l))

# mylist=["Ali", "Hamdan", "Yousaf", "Sufyan", "Anas"]
# if "Hamdan" in mylist:
#     print("yes, Hamdan in this list")

# mylist=["Ali", "Hamdan", "Yousaf", "Sufyan", "Anas"]
# mylist[2:4]=["Imran", "bhatti"]
# print(mylist)

# type=["id","ahmad","safi","ali"]
# type.insert(3,"Imran")
# print(type)
#Append in list
# list=["Ali","Hamza","yousaf"]
# list.append("Imran")
# print(list)

# #insert:
# list=["ALI","HAMZA","YOUSAF","ROHAN"]
# list.insert(2,"IMRAN")
# print(list)

#Extend:
# myname=["Summaiya","BIBI"]
# my_age=["25 years"]
# myname.extend(my_age)
# print(myname)

#extend using iterable: tuple b list mai extend ho sakhti hai
# roman=["gul", "Asad","Ali","rimla"]
# name=("saba"," Muqadas")
# roman.extend(name)
# print(roman)

#remove method in list:
# roman=["gul", "Asad","Ali","rimla"]
# roman.remove("gul")
# roman.remove("Asad")
# print(roman)

# roman=["gul", "Asad","Ali","rimla"]
# roman.pop(2)
# print(roman)

#del this list index:
# roman=["gul", "Asad","Ali","rimla"]
# del roman[0]
# print(roman)

#clear this list:
# roman=["gul", "Asad","Ali","rimla"]
# roman.clear()
# print(roman)

# roman=["gul", "Asad","Ali","rimla"]
# for a in roman:
    # print(a)

#len;
# a=["ahad", "ali", "hamza", "sfii"]
# for l in range(len(a)):
#     print(a[l])

# myname=["ahad", "ali", "hamza", "sfii"]
# i = 1
# while i < len(myname):
#     print(myname[i])
#     i=i+1

# #list comprehension:
# intlist=["Summaiya","Gull","Bibi"]
# # [print(x) for x in intlist]

# i=1
# while i< len(intlist):
#     print(intlist[i])
#     i=i+1

# List Comprehension: is mai value b miss kr kai likh sakhty hai:
# myFirstDay=["boring","working","Amazing","difficult"]
# svalue=[]
# for x in myFirstDay:
#     if "o" in x:
#         svalue.append(x)
# print(svalue)
 

myname=["Summaiya","gull","bibi"]
days=[a for a in myname if "a" in a]
print(days)






























































































































































