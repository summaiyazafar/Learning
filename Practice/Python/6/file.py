# print("hello world!")
# for n in range(8):
    # print("Summaiya")
# for p in range(1,11):
    # print("2*",p,"=",2*p)
# for k in range(10,0,-1):reverse form
    # print("10*",k,"=",2*k)

# i=1 #inverse function
# while i<=10:
#     print("Summaiya")
#     i=i+1
# print(i)

# p=10 #reverse function
# while p>=1:
#     print("bibi")
#     p=p-1
# print(p)

# e=7
# while e>=2:
#     print("Sadiqa")
#     e=e-1
# print(e)

# g=2
# while g<=6:
#     print("Insha")
#     g=g+1
# print(g)
#Dictionary method: ordered changeable or not duplicateable
mydict={"myname":"Summaiya Bibi", 
        "Student id": "bc210403887",
        "Study_plan": "BSCS"}
# print(mydict) #simple print
# print(len(mydict)) #print length
# print(mydict["myname"]) #single keys print
# print(mydict.get("Student id")) #get 1 keys value
# y=mydict.keys()   #keys value
# print(y)
# x=mydict.values()
# print(x)
# z=mydict.items()
# print(z)
# mydict["myname"]="Gull"
# z=mydict.items()
# print(z)
# if statement:
# mydict={"myname":"Summaiya Bibi", 
#         "Student id": "bc210403887",
#         "Study_plan": "BSCS"}
# if "myname" in mydict:
#     print("Yes,'gull' is available in mydict.")
# mydict={"myname":"Summaiya Bibi",  
#         "Student id": "bc210403887",
#         "Study plan": "BSCS"}
# update method:
# mydict.update({"myname":"Gull","Student id":"Nothing","Study plan":"BSIT"})#update method in dictionary
# print(mydict)
#change method
# mydict["Student id"]="nothing"#change method
# print(mydict)
mydict={"myname":"Summaiya Bibi",  
        "Student id": "bc210403887",
        "Study plan": "BSCS"}
#add method:
# mydict["myage"]=24
# print(mydict)

#update method:
# mydict.update({"Myage":25})
# print(mydict)

#pop method:
# mydict.pop("myname")
# print(mydict)

#popitem() method: yeh last wali key delete kr deta hai
# mydict.popitem()
# print(mydict)

# del() (specific key) method:
# del mydict["myname"]
# print(mydict)

#del() all delete dictionary:
# del mydict
# print(mydict)

# clear() method:
# mydict.clear()
# print(mydict)

# for x in mydict:     #yeh sirf keys print kry ga
#     print(x)

# for x in mydict:
#     print(mydict[x])#yeh sirf values ko print kry ga

# for key in mydict.keys():#2nd method
#     print(key)

# for value in mydict.values(): 2nd method
#     print(value)

# for key, value in mydict.items(): key or value ik sath print krwana
#     print(key, value)

#copy method in dictionary:
# thisdict=mydict.copy() #copy method
# print(thisdict)

# thisdict=dict(mydict)#copy method
# print(thisdict)

#Nested dictionary: 1st method
# myfile= {
#     "child1":{
#         "name":"hasan",
#         "id":"22222",
#         "CNIC":333333333
#     },
#     "child2":{
#         "name":"Ahsan",
#         "id":444,
#         "CNIC":88888
#     },
#      "child3":{
#         "name":"mohsin",
#         "id":0000,
#         "CNIC":11111
#         }
# }
# print(myfile)

#2nd method:
# child1={
#         "name":"ali",
#         "id":2222,
#         "CNIC":333333333
# }
# child2={
#         "name":"zain",
#         "id":5555,
#         "CNIC":4444
#         }
# child3={
#         "name":"hasan",
#         "id":1111,
#         "CNIC":3337777
# }
# formatedfile= {
#     "child1":child1,
#     "child2":child2, 
#     "child3":child3
# }
# # print(formatedfile)
# # print(formatedfile["child1"]["name"])

# #nested dictionary using items:
# child1={
#     "name":"anaya",
#     "id":2222,
#     "age":22
# }
# child2={
#     "name":"aiza",
#     "id":22332,
#     "age":23
# }
# child3={
#     "name":"ashmil",
#     "id":6666,
#     "age":24
# }
# formal={
#     "child1":child1,
#     "child2":child2,
#     "child3":child3
# }
# print(formal)

# for x, obj in formal.items():
#     print(x)
#     for y in obj:
#         print(y + ': ',obj[y])

# a = 2
# b = 33
# print("A") if a < b else print("B")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

#Match statement:
# day=5
# match day:
#     case 1:
#         print("wednesday")
#     case 2| 3| 4|5:
#         print("thursday")

# while Loop 
# w=1
# while w < 6:
#     print("Summaiya")
#     if w==3:
#         break
#     w=w+1
# o=1
# while o < 9:
#     o+=1
#     if o==6:
#         continue
#     print(o)
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# day=4
# month=7
# match day:
#     case 1|2|3|4|5|6|7 if month==4:
#         print("I am happy now")
#     case 1|2|3|4|5|6|7 if month==5:
#         print("Today is the rainy day")
#     case _ :
#         print("Stop working now")

# i=0
# while i < 5:
#     print(i)
#     if i == 4:
#         break
#     i+=1

# p=1
# while p < 10:
#     p+=1
#     if p==7:
#         continue
#     print(p)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break
# for x in "banana":
#     print(x)




































































































