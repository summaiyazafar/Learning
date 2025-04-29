# mymodule.py 
# def greeting(name):
#     print("Hello!", name)
# import mymodule
# mymodule.greeting("Gull")
# mymodule.py
#just print in one time:
# def greeting(name):
#     print("Hello!" , name)
# if __name__=="__main__":
#     greeting("Gull")

# person1 = {
#   "name": "Summaiya",
#   "age": 24,
#   "country": "Pakistan"
# }
# from mymodule import person1
# print(person1["age"])
# a=mymodule.person1["age"]
# print(a)
# # if __name__ == "__main__":
# #     print(person1["age"])


# import platform
# x=platform.system()
# # print(x)
# x=dir(platform)
# print(x)

#Datetime concept in python
# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.strftime("%A"))
# print(x.strftime("%B"))

# import datetime
# x=datetime.datetime(2025,4,28)
# print(x.strftime("%A,%d.%B.%Y"))

#Maths:min(), max(), abs(), aur pow() built-in functions hain jo simple mathematical operations perform karte hain.
# x=min(22,3,44)
# print(x)

# x=max(22,33,44)
# print(x)

# x=abs(-22)
# print(x)

# x=pow(8,2)
# print(x)
# math.sqrt(), math.ceil(), math.floor(), aur math.pi jaise methods aur constants math module 
# mein available hain jo advanced mathematical operations perform karne mein madad karte hain.
# import math
# x=math.sqrt(16)
# print(x)

# x=math.ceil(1.8)
# y=math.floor(1.8)
# print(x)
# print(y)

# x=math.pi
# print(x)


# #json(javascript Object Notation)
# import json
# # ek Python object (dictionary):
# x = '{"name":"summaiya","age": 24,"city": "pakistan"}'
# # y = json.dumps(x)# Python object ko JSON mein convert karo:
# # print(y)# ab y ek JSON string hai:
# y=json.loads(x)
# print(y["name"])

# json.loads() ka use JSON string ko Python object mein convert karne ke liye hota hai.
# json.dumps() ka use Python object ko JSON string mein convert karne ke liye hota hai.
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # Result ko readable banane ke liye indentation use karo:
# print(json.dumps(x, indent=4, sort_keys=True))


# username=(input("Enter the name: "))
# print("User name is", username)

# price = 49
# txt = "The price is {} dollars"
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# f_string ka use:
# degree="BSIT"
# myname="Summaiya bibi"
# age=24
# data="My name is {}, my age is {} and my study plan is {}."
# print(data.format(myname,age,degree))


# f = open("demofile.txt")  # File open karna
# print(f.read())           # File ka content print karna

# with open("demofile.txt") as f:
#   for x in f:
#     print(x)









