# import numpy as np 
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr=arr.flaten()
# print(up_arr)
# print(arr)


# # ravel 
# import numpy as np 
# # example 2d 
# arr = np.arange(14).reshape(7,2)
# print(arr)
# up_arr=arr.ravel()
# print(up_arr)

# "import numpy; print(numpy.__version__)"
# python -m venv .venv
# .venv\Scripts\activate
# pip install numpy

# transpose 
# import numpy as np 
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr=arr.transpose
# print(up_arr)
# print(arr)



# slicing
# import numpy as np 
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr=arr.[:3]
# print(up_arr)



# slicing for 2d
# import numpy as np 
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr=arr.[:,-1]
# print(up_arr)

# while loop 
import numpy as np
arr = np.arange(12)
i=0
while i<len(arr):
    print(arr[i], end="")
    i+=1

# while loop 2d 
import numpy as np
arr = np.arange(12).reshape(3,4)
i=0
while i<learn(arr):
    j=0
    while j < len(i):
        print(arr[i][j] , end= "" )
        