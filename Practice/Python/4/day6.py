#While loop: reverse
# i=10
# while i>=1:
#     print("Summaiya")
#     i=i-1
# print(i)
# i=1
# while i<=10: inverse function
#     print("Python")
#     i=i+1
# print(i)

# string immutable
# w=("Summaiya bibi")
# print(w[-1])
# # print(w[0::2])#string mai slice inverse form mai
# print(w[-1::-2])#string indexing mai slice in reverse form

# string iteration
# s=("My name is Summaiya")
# t=len(s)
# print(t)
# for a in range(t):
#     print(s[a])#inverse form
    
# w=("My first day is at last day")
# t=len(w)
# print(t)
# for e in range(t-1,-1,-1):
    # print(w[e])#reverse form

# lower upper captilize title
# s=("My name is Summaiya")
# n=s.upper()
# print(n)

# A=("Summaiya")
# print(A.find("a"))

#python chr() ord():
#chr()
# y=65#integer to character
# print(chr(y))

# ord()
# y="B"
# print(ord(y))#character to 

#String format:is mai >left side space kai liyee 
# <right side space kai liyee ^ mid ki space kai liyee use hota
# s=("My name {} Summaiya {} my {} is {}".format("is","and","age",24))
# print(s)
# t=("My name {0} Summaiya {1} my {2} is {3}".format("is","and","age",24))
# print(t)
# z=("My name {a:>11} Summaiya {b:<10} my {c:^6} is {d:4}".format(a="is",b="and",c="age",d=24))
# print(z)

# d=("My {a:^2} program {b:^2} AI and {c:^3} age {d:^4} {e:^6}".format(a="study",b="is",c="my",d="is",e=24))
# print(d)

#List mai slicing or mutable mean changeable:
# l=[10, 20, 30, 40,50,60,70]
# print(l[3])#inverse form
# print(l[0:3])
# print(l[2::2])
# print(l[1::4])
# print(l[3:])
# print(l[-1::-3])#reverse form
# print(l[-1::-1])

#list using iteration:
# l=[10,20,30,40,50,60]
# t=len(l)
# print(t)
# for a in range(t-1,-1,-1):
#     print(l[a])#inverse form
# for a in range(t):
#     print(l[a])#reverse form

#List Comprehension:
#append in list
# s=[]
# for a in range(1,100):
#     s.append(a)
# print(s)
# j=[k for k in range(1,100) if k%5==0]
# print(j)

# h=("Summaiya")
# k=[g for g in h]
# print(k)

# l=[50,60,70,80,90,100]
# del l[1] #delete function
# print(l)
# print(l.pop(3))#pop mai jo delete krta hai value woh sath btata b hai
# print(l)
# l.remove(60)#vlue remove krta hai
# print(l)
# l.clear()#purhi value clear ho jati hai
# print(l)
# update value:
l=[50,60,70,80,90,100]
# l[0]=40
# print(l)#yaha pehli value change ho jati hai
# insert:
# l.insert(0,10)#jitni value hon utni tk insert ho sakhti hai value
# print(l)
#append
# l.append(70)#append jo hm new value likhty hai woh last py ja kai create hoti hai 
# print(l)
# n=[50,60] jessa data hm dety hai wesy he last py dal deta hai
# l.append(n)
# print(l)
# n=[30,110]
# l.extend(n)#value dein lakin last py dal toh deta hai lakin pr acha work krta hai
# print(l)






















































































































