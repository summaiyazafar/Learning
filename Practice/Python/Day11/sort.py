import numpy as np
arr=np.array([2,6,1,4,3,5,8,7])
new=np.sort(arr)
print(new)

import numpy as np
arr=np.array(["Orange", "Apple" , "Grapes", "Banana"])
newarray=np.sort(arr)
print(newarray)

#2-D array:
import numpy as np
spider=np.array([[1,3,2,6,5],[4,7,8,6,9]])
new=np.sort(spider)
print(new)

#bool sort mai false wali value hmesha pehly print hoti f pehly aata t sy
import numpy as np
boolean=np.array([True, False, False, True,False, True])
print(np.sort(boolean))
