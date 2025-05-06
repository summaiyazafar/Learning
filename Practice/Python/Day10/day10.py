#pyplot 
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("data.csv")
# df.plot()
# plt.show()


#Scatter plot
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("data.csv")
# df.plot(kind="scatter", x="Duration", y="Calories")
# plt.show()

#Histogram
import pandas
import matplotlib.pyplot as plt
df=pandas.read_csv("data.csv")
df["Duration"].plot(kind="hist")
plt.show()
