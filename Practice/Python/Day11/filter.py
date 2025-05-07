# import numpy as np
# num=np.array([1,2,3,4,5])
# sm=[True, True,True, True,False]
# new=num[sm]
# print(new)   filtering mai true ka use kiya jata hai aghr ks element ki value nikalni hoti hi

#condition use in filtering:
# import numpy as np
# arr=np.array([2,3,4,5,6,7])
# filter_array=[]
# for x in arr:
#     if x >2:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)
# newarray=arr[filter_array]
# print(filter_array)
# print(newarray)

#Even num run krwany kai liyee:
# import numpy as np
# arr=np.array([2,3,4,5,6,7])
# filter_array=[]
# for x in arr:
#     if x %2==0:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)
# newarray=arr[filter_array]
# print(filter_array)
# print(newarray)

# odd number kai liyee filtering system:
# import numpy as np
# arr=np.array([2,3,4,5,6,7])
# filter_array=[]
# for x in arr:
#     if x %2==1:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)
# newarray=arr[filter_array]
# print(filter_array)
# print(newarray)

#Shortcut filtering system:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9])
# filter_array= arr < 9
# new_filter=arr[filter_array]
# print(filter_array)
# print(new_filter)