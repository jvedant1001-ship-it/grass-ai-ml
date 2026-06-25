# # import numpy as np

# # arr = np.array([1, 2, 3, 4, 5])
# # print(arr)

# # import numpy as np

# # print(np.__version__)

# import numpy as np

# arr2 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(arr2)
# arr2[1][0]=100
# print(arr2)

# # import numpy as np

# # arr1 = np.array([1, 2, 3, 4, 5])
# # arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# # print(arr1.ndim)  # 1
# # print(arr2.ndim)  # 2


# import numpy as np
# # time taken by list and array
# import time
 
# # List timing
# start = time.time()
 
# l = [i * 2 for i in range(1000000)]
 
# end = time.time()
# print("Time taken by list:", end - start)
 
# # NumPy array timing
# start = time.time()
 
# a = np.array(1000000) * 2
 
# end = time.time()
# print("Time taken by array:", end - start)
 



# #for zeros

# import numpy as np
# arr = np.zeros(5)
# print(arr)
# arr1 = np.zeros((3,4))
# print(arr1)



# # for ones
# import numpy as np
# arr = np.ones(5)
# print(arr)
# arr1 = np.ones((3,4))
# print(arr1)




# zeros ka use krke 2d array bnana h 

# import numpy as np
# #2 d array of zeros
# arr = np.zeros((5,5))
# print(arr)
# # 2 d array inc by 10
# arr = np.zeros((5,5))+10
# print(arr)

#1 d full

# import  numpy as np
# arr=np.full((3),3)
# print(arr)

# #2d full

# import  numpy as np
# arr=np.full((3,5),3)
# print(arr)



# # by the help of full 2d matrix of one's
# import  numpy as np
# arr=np.full((5,5),1)
# print(arr)

# # by the help of zero's 2d matrix of value 6
# import  numpy as np
# arr=np.zeros((5,5))+6
# print(arr)


# # radnom 1d 

# import numpy as np
# arr = np.random.rand(5)
# print(arr)

# #random 2d

# import numpy as np
# arr = np.random.rand(5,3)
# print(arr)


# arrange for 1 d 

# import numpy as np

# arr = np.arange(5,3)
# print(arr)

# #vector 1d list           




# import numpy as np

# # Vector (1D list)
# l = [1, 2, 3, 4]
# print("1D List:", l)

# # Vector (1D array)
# a1 = np.array([1, 2, 3, 4])
# print("1D Array:")
# print(a1)

# # Matrix (2D list)
# m = [[1, 2, 3, 4],
#      [5, 6, 7, 8]]
# print("2D List:", m)

# # Matrix (2D array)
# a2 = np.array(m)
# print("2D Array:")
# print(a2)

# # 3D list
# t = [[[1, 2],
#       [3, 4],
#       [5, 6],
#       [7, 8]]]
# print("3D List:", t)

# # 3D array
# a3 = np.array(t)
# print("3D Array:")
# print(a3)

# # Dimensions
# print("a1 dimensions:", a1.ndim)
# print("a2 dimensions:", a2.ndim)
# print("a3 dimensions:", a3.ndim)

# # Shapes
# print("a1 shape:", a1.shape)
# print("a2 shape:", a2.shape)
# print("a3 shape:", a3.shape)


# mport numpy as np
# # vector 1d list
# l = [1,2,3]
# print(l)
# #vector 1d array
# arr = np.array(l)
# print(arr)
 
# #matrix 2d list
# l = [[1,2,3],[4,5,6]]
# print(l)
# #matrix 2d array
# arr = np.array(l)
# print(arr)
 
# #tensor 3d list
# l = [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l)
# #tensor 3d array
# arr = np.array(l)
# print(arr)
 


 