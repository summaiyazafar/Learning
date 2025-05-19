# name=["Shams","Qamar","Husain","Raza","Mudaser","Anas","Zain"]
# correct_rgba = rgba[:]
# correct_rgba[-1] = "Alpha"
# print(correct_rgba)

# name=["Shams","Qamar","Husain","Raza","Mudaser","Anas","Zain"]
# newname=name
# id(name)==id(newname)
# newname.append("Maan")
# print(newname)

# letters=["A","B","C","D","E","F","G"]
# print(len(letters))
# letters[2:6]=["c","d","e","f"]
# print(letters)
# letters[2:5]=[]
# print(letters)
# letters[:]=[]
# print(letters)

# a=["a","b","c","d","f"]
# b=["g","h","i","j","k"]
# x=[a,b]
# x[0][1]
# print(x)

marks=[10,20,30,40,50]
# new_marks=[]         #long method
# for x in marks:
#     new_marks.append(x+2)
# print(new_marks)

# new_marks=[x-2 for x in marks]# comprehension method
# print(new_marks)

cube=[]
# for x in range(11):
#     if x %2==0:
#         cube.append(x**3)
# print("Using for loop:", cube)

list=[x**3 for x in range(10) if x%2==0]
print(list)




