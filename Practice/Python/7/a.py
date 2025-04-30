
import pandas
s=pandas.read_csv("data.csv")
p=s.dropna()
print(p.to_string())








