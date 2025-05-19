# x=int(input("Enter the value:"))
# if x>=0:
#     print("X greater than zero")
# elif x<0:
#     print("X is less than zero")
# elif x==0:
#     print("X is equal to zero")
# else:
#     print("More")

# words=["ALI","HAMZA","USAMA","KHIZAR"]
# for w in words:
#     print(w, len(w))

# words=["ALI","HAMZA","USAMA","KHIZAR"]
# for i in range(len(words)):
#     print(i, words[i])

# list=range(10)
# for x in list:
#     if x==6:
#         break 
#     print(x)

# for x in range(2,10):
#     for n in range(2, x):
#         if x%n ==0:
#             print(f"{x} equal {n}* {x//n}")
#             break

# for num in range(0, 10):
#     if num % 2==0:
#         print(f"Even num{num}")
#         continue
#     print(f"odd num{num}")

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x} ")
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# for x in range(2,10):
#     if x ==6:
#         continue
#     print(x)

for n in range(0,11):
    if n%2 == 0:
        continue
    print(f"odd num {n}")
else:
    print(f"even number {n}")