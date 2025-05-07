# yaha check kr rahy hai 4 kis kis index py parha hua hai
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,4,9,4])
# newarray=np.where(arr==4)
# print(newarray)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9])
# newarray=np.where(arr%2==0)#even kai liyee 
# newarray1=np.where(arr %2==1)#odd kai liyee
# print(newarray)
# print(newarray1)

# import numpy as np
# new=np.array([1,2,3,4,5])
# arr=np.where(new==2)#yaha check krna 2 kis index py parha hua hai
# print(arr)

#hm index check krny kai liyee side ka b use kr sakhty hai:
# import numpy as np 
# new=np.array([1,2,3,4,5])
# arr=np.searchsorted(new, 2, side="left")#yaha searchsorted ka use hota hai
# arr=np.searchsorted(new, 2, side="right")
# print(arr)

#Searchsorted jo hota yeh ascending order mai hota hai:
import numpy as np
arr=np.array([1,3,5,7,9])
newarray=np.searchsorted(arr, [2, 4, 6, 8])
print(newarray)