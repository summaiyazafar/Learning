#copy or view mai faraq
# import numpy as np
# arr=np.array([1,2,3,4,5])        copy method mai original change nai hota 
# x=arr.copy()
# x[2]=32
# print(x)
# print(arr)

# import numpy
# arr=numpy.array([1,2,3,4,5])    #view method mai ik mai chan ging krein toh dosri khud ba khud change ho jati hai
# x=arr.view()
# x[2]=22
# print(arr)
# print(x)

#check which array is copy() or view() so we use .base method
import numpy as np
arr=np.array([1,2,3,4,5])
s=arr.copy()#copy base method mai none return return krta hai
v=arr.view()#or view jo vaue de hue hoti hai woh return krta hai
print(s.base)
print(v.base)