# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([4,5,6])
# arr=np.concatenate((arr1 , arr2))
# print(arr)

# import numpy as np
# arr1=np.array([[1,2,3,4],[5,6,7,8]])
# arr2=np.array([[1,2,3,4],[5,6,7,8]])
# arr=np.concatenate((arr1 , arr2), axis=1)
# print(arr)

# Stack function in concatenate:
# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]])
# arr2=np.array([[7,8,9],[10,11,12]])
# arr=np.stack((arr1, arr2), axis=1)
# print(arr)

# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# arr=np.stack((arr1, arr2), axis=1)
# print(arr)
# arr=np.hstack((arr1, arr2))#horizental stack
# print(arr)
# arr=np.vstack((arr1, arr2))#vertical stack
# print(arr)
# arr=np.dstack((arr1, arr2))#depth stack or hight along stack
# print(arr)