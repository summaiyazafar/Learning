# name=input()
# print("Hello", name, 'how are you?')

# PersonA_name=input("Enter your name: ")
# PersonA_age=input("Enter your age: ")
# PersonB_name=input("Enter your name: ")
# PersonB_age=input("Enter your age: ")
# if PersonA_age < PersonB_age:
#     print(PersonA_name, " is younger then", PersonB_name)
# else:
#     print(PersonA_name, " is older then", PersonB_name)

#BMI calculator ask name, weight and hight:
PersonA_name=input("Enter your name:")
PersonA_Weight=float(input("Enter your kg: "))
PersonA_Height=float(input("Enter your cm:"))
Height=PersonA_Height/100
weight=PersonA_Weight/Height**2
print(f"{PersonA_name}, your BMI is {weight:.2f}")
if weight < 10.2:
    print("You need to loss your weight")
else:
    print("you are normal") 