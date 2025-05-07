#2D Array:
# import numpy as np
# arr=np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(arr.shape)

#5D Array:
# import numpy as np
# arr=np.array([1,2,3,4], ndmin=5)
# print(arr)
# print("Shape of Array:", arr.shape)


#Reshaping Concept:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,0])
# df=arr.reshape(5,2)
# print(df)

#1D TO 3D:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarray=arr.reshape(2,2,3)
# print(newarray)

#Copy or view method in reshape:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(4,2).base)# yeh ik view hai

#unkown diamention
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# newarr=arr.reshape(2,2,-1)
# print(newarr)

#Flattening the array which mean multidiamentional convert into 1D array 
# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# newarr=arr.reshape(-1)
# print(newarr)

#numpy array iterator
# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# for x in arr:
#     for y in x:
#         print(y)

# import numpy as np
# arr =np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])

# # for x in arr:
# #   print("x represents the 2-D array:")
# #   print(x)

# for x in arr:
#     for y in x:
        print(y)
        # for z in y:
        #     print(z)





























