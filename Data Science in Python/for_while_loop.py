# #for loop: more use and repeatation task is for loop can replace
# name=["Ali","Hasan","Irtaza","Ahmad","Yousaf","Hmadan"]
# for index, item in enumerate(name, start=0):
#     print(f"{index}.{item}")

# #foods:
# menu=["Biryani","Haleem", "Dahi Bhaly", "Daal","Mixed Vegitables"]
# for index,  food in enumerate(menu, start=1):
#     print(f"{index}.{food}")

# menu=["Biryani","Haleem", "Dahi Bhaly", "Daal","Mixed Vegitables"]
# for food in menu:
#     print(food)

# #Flowers:
# Flowers=["Red rose", "Yellow rose", "Pink rose", "Purple rose", "Orange rose"]
# for index, rose in enumerate (Flowers, start=1 ):
#     print(f"{index}.{rose}")

# Flowers=["Red rose", "Yellow rose", "Pink rose", "Purple rose", "Orange rose"]
# for rose in Flowers:
#     print(rose)

# girls_name=["Humna", "Momina","Saweira", "Ayesh Fatime"]
# for index, names in enumerate(girls_name, start=1):
#     print(f"{index}.{names}")

#While loop:
# i=0
# while i < 10:
#     print(i)
#     i+=1

#break statement:
for letter in "python":
    if letter == "h":
        break
    print(letter)

#Continue statement:
for letter in "python":
    if letter == "o":
        continue
    print(letter)

#pass statement:
for letter in "python":
    if letter == "o":
        pass
    print(letter)