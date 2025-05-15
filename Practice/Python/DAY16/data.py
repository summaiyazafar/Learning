# s = 'supercalifragilisticexpialidocious'
# print(len(s))
# print(s[-3:-1])

# # squares = [1, 4, 9, 16, 25]
# # p=squares+[1, 4, 9, 16, 25]
# # print(p)
# cubes = [1, 8, 27, 65, 125]  # something's wrong here
# 4 ** 3  # the cube of 4 is 64, not 65!
# cubes[3] = 64  # replace the wrong value
# cubes.append(216)  # add the cube of 6
# cubes.append(7 ** 3)  # and the cube of 7
# print(cubes)

# squres=[1,2,4,8,16,30]
# squres[5]=32
# squres.append(64)
# squres.append(64*2)
# print(squres)

# Alpabet=["a","b","c","d","e","f","g"]
# Alpabet.append("h")
# Alpabet[1:3]=["B","C"]
# # print(Alhabet)
# Alpabet[4:8]=[]
# # print(Alhabet)
# # Alpabet[:]=[]
# # print(Alpabet)#clear 
# print(len(Alpabet))

# a=[1,2,3,4,5]
# b=['a','b','c',"d",'e']
# x=[a,b]
# # print(x)
# x[0][1]
# print(x)

# a, b = 0 , 1
# while a < 500:
#     print(a, end=",")
#     a, b= b, a+b   febonnic series

# s=int(input("Enter the value:"))
# if s<0:
#     print("Shallow")
# elif s<1:
#     print("Greater value")
# elif s==0:
#     print("Equal value")
# else:
#     print("Nothing will be print")

#Measuring the length of the word:
# s=['Summaiya', 'Gull', 'Maan']
# for w in s:
#     print(w, len(w))

# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# s=[1,2,3,4,5,6]
# for i in range(len(s)):
#     print(i, s[i])
# s=sum(range(4))
# print(s)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
for n in range(2,8):
    for x in range(2,n):
        if n% x==0:
            print(f)














