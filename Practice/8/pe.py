# import pandas as pd
# df=pd.read_csv('d2.csv')
# new_df=df.dropna()
# print(new_df.to_string())



import pandas as pd
df=pd.read_csv("d2.csv")
df["Date"]=pd.to_datetime(df["Date"], format="mixed")
df.dropna(subset=["Date"], inplace=True)
print(df.to_string())