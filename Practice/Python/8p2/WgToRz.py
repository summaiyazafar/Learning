# # bymistake edit hue value ko set krna 
# # import pandas as pd
# # df=pd.read_csv('data.csv')
# # df.loc[7, 'Duration']=45
# # print(df.to_string())

# #barhi value ko chota krna ya equal krna

# import pandas as pd
# df = pd.read_csv('data.csv')
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] = 120
# print(df.to_string())

#drop method
# import pandas as pd
# df=pd.read_csv('data.csv')
# for x in df.index:
#     if df.loc[x, "Duration"]>120:
#         df.drop(x, inplace=True)
# print(df.to_string())


#duplicate method:
# import pandas as pd
# si=pd.read_csv("data.csv")
# print(si.duplicated()) #yaha ans false show hota hai

#drop method: yaha same data remove ho jata hai
# import pandas as pd
# df=pd.read_csv("data.csv")
# df.drop_duplicates(inplace=True)
# print(df.to_string())

