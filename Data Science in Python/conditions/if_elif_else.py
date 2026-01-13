# grades=78
# if grades >=70:
#     print("you are intelligent")
# elif grades <=50:
#     print("you are satisfactory student")
# else:
#     print("Fail")


# x=["Ali", "Khizar", "Ahmad"]
# for w in x:
#     print(w, len(w))

# for x in range(5):
#     print(x)

# for n in range (2,12):
#     for x in range(2, n):
#         if n%x==0:
#             print(f"{n} is equal {x} * {n//x}")
#             break

# for num in range(2,10):
#     if num %2 == 0:
#         print(f"found a even number {num}")
#         continue
#     print(f"found a odd num {num}")

for x in range(2,13):
    for n in range(2,x):
        if x%n==0:
            print(x, 'equals', x, '*', x//n)
            break
    else:
        print(x, 'is prime number ')