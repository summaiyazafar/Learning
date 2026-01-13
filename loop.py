# for x in range(10):
#     print("Summaiya")

# i=1
# while i <6:
#     print("Summaiya")
#     i+=1

# i=1
# while i<10:
#     print("Summaiya")
#     if(i==9):
#         break
#     i+=1

# def myfunc(name,degree):
#     print(f"My name is {name} and my degree is {degree}.")
# myfunc("Summaiya","BSCS")

# def myfunc(a,b):
#     total=a+b
#     return total
# count=myfunc(3,17)
# print(count)

# def local():
#     name="Summaiya"
#     print(f"my name is {name}")
# local()

a=10
def globalv():
    global a
    print(f"inside a function {a}")
globalv()
print(f"outside a function {a}")