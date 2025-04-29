#pandas libraries:
# import pandas as pd
# gul={
#     "Subject":["Math","S.Study","English"],
#     "Number":[80, 70, 90]
# }
# myvar=pd.DataFrame(gul)
# print(myvar)

# import pandas as pd
# a=[1,2,3,4]
# myvar=pd.Series(a,index=["s", "d", "w", "o"])
# print(myvar)
# print(myvar["w"])#return kai liyee

# import pandas as pd
# b={"summaiya age":24 , "student level": "bscs"}
# myvar=pd.Series(b, index= ["summaiya age" , "student level"])
# print(myvar)

import pandas as pd
gull={
    "Student name": ["Sundas", "Saba", "Sumbal"],
    "Student id": [1, 2, 3]
}
myvar=pd.DataFrame(gull)
print(myvar)
