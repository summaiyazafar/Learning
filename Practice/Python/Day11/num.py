# import numpy as np
# df=np.array([1,2,3,4,5])
# print(np.__version__)
# print(df)
# import numpy as np
# arr=np.array((1,2,3,4))
# print(arr)


#checking Diamentions:
# import numpy as np
# a=np.array(22)
# b=np.array([1,2,3,4,5])
# c=np.array([[1,2,3], [4,5,6],[7,8,9]])
# d=np.array([[[1,2,3],[4,5,6], [1,2,3]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# import numpy as np#5-diamentional array
# arr=np.array([1,3,5,7,9], ndmin=5)
# print(arr)
# print("Number of diamentions is :", arr.ndim)

# indexing in array:
#  import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr[0])

# import numpy as np
# arr=np.array([[1,2,3,4,5,6],[7,8,9,0,1,2]])
# print(arr[0,1])

# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr[2] +arr[3])

# import numpy as np
# arr=np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1]])
# print(arr[0,-4])
# print(arr[1,-4])
# print(arr.ndim)


# #Slicing:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(arr[2:])#2 sy ownward
# print(arr[:2])#2 sy pehly waly
# print(arr[-3: -1])#backword
# print(arr[0:7:3])#start end step
# print(arr[::3])#2 2 ka gap sy

#2D Array:
# import numpy as np
# arr=np.array([[1,2,3,4,5,6,7],[7,6,5,4,3,2,1]])
# print(arr[1,1:4])

import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr.dtype)
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')  # ya astype(int)
# print(newarr)
# print(newarr.dtype)
# arr=np.array([1,2,3,4,5])
# df=arr.astype("f")
# print(arr)
# print(df)
# print(arr.dtype)
# print(df.dtype)