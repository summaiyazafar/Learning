# from numpy import random
# x=random.randint(10)
# print(x)

# from numpy import random
# s=random.rand(10)
# print(s)

# from numpy import random
# d=random.randint(10, size=5)
# print(d)

# from numpy import random
# f=random.randint(12, size=(3,4))
# print(f)

#Choice method:
# from numpy import random
# x=random.choice(10)
# print(x)

#Data distribution in random
# from numpy import random
# x=random.choice([3,5,7,9], p=(.0, .5, .2, .3), size=(10))
# print(x)

#shuffle
# from numpy import random
# import numpy as np
# arr=np.array([1,2,3,4,5])
# random.shuffle(arr)
# print(arr)

#Permutation:
# from numpy import random
# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(random.permutation(arr))

#Seoborn matplotlib:which make graph

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot([0,3,5,9], kind="kde")
# plt.show()

#normal graph 
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# # sns.displot(random.normal(loc=2, scale=5, size=(2,3))) #yeh essy b likha ja sakhta hai or jo nichy line likhi wesy b
# sns.displot(random.normal(size=1000), kind="kde")  # kde sy bell curve bnti hai
# plt.show()     #1000 ka mtlb random value kuch b generate ki gai hai

# Bionomial distribution(discrete distribution which mean countable task)
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(random.binomial(n=10, p=0.5, size=7))
# plt.show() 


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data={
    random.normal(loc=2, scale=0.5, size=10),
    random.binomial(n=10, p=0.5, size=10)
}
sns.displot(data, kind="kde")
plt.show()