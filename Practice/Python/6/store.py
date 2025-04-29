# with open("demofile.txt", "a") as f:
#   f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read())

# import pandas as pd
# mydataset={
#     'car':["BMW","Honda","Lemozeen"],
#     'passing':[3,2,4]
# }
# myvar=pd.DataFrame(mydataset)
# print(myvar)

# import pandas as pd
# print(pd.__version__)

# import pandas as pd
# a=[2,3,4]
# myvar=pd.Series(a)
# print(myvar)
# print(myvar[1])

# import pandas as pd
# a=[2,3,4,5]
# s=pd.Series(a, index=["x","y","z","s"])
# print(s)

#series is one dimentional or signal coloumn
# import pandas as pd
# dict={"day1":10,"day2":20,"day3":30}
# mylist=pd.Series(dict, index=["day1","day2"])
# print(mylist)

#dataframe is multi dimentional(data structure):
# import pandas as pd
# d={
#     "Student name":["Ali","Hasan","Zain","Abid"],
#     "Study plan": ["BSIT","BS-Eng","BSCS","BS_Software Engineer"]
# }
# df=pd.DataFrame(d)
# myvar=df.loc[df["Student name"]=="Ali","Abid"]
# print(myvar)


# import pandas as pd
# d = {
#     "Student name": ["Ali", "Hasan", "Zain", "Abid"],
#     "Study plan": ["BSIT", "BS-Eng", "BSCS", "BS_Software Engineer"]
# }
# # Step 1: Pehle DataFrame banao
# df = pd.DataFrame(d)
# # Step 2: Ali ki row dhoondo
# myvar = df.loc[df["Student name"] == "Ali"]
# print(myvar)

#findall
# import re 
# txt="imran bhatti"
# x=re.findall("i", txt)
# print(x)

#split
# import re 
# txt="imran bhatti"
# x=re.split("\s", txt)
# print(x)

#search:
# import re
# s="My name is Summaiya Zafar."
# w=re.search("\s", s)
# print("Number of words:", w.start())

# 
import pandas as pd

data = {
  "Duration": {
    "0": 60,
    "1": 60,
    "2": 60,
    "3": 45,
    "4": 45,
    "5": 60
  },
  "Pulse": {
    "0": 110,
    "1": 117,
    "2": 103,
    "3": 109,
    "4": 117,
    "5": 102
  },
  "Maxpulse": {
    "0": 130,
    "1": 145,
    "2": 135,
    "3": 175,
    "4": 148,
    "5": 127
  },
  "Calories": {
    "0": 409,
    "1": 479,
    "2": 340,
    "3": 282,
    "4": 406,
    "5": 300
  }
}

df = pd.DataFrame(data)

print(df)

















