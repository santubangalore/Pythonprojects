from numpy import *

arr1= array([
            [1,2,3,5,9,10],
            [4,6,8,11,13,15]
            ])

print(arr1.ndim)

print(arr1.shape)

arr2=arr1.flatten()

print(arr2)

arr3= arr2.reshape(3,4)

print(arr3)

#two two-d arrarys of 2X3
arr3= arr2.reshape(2, 2, 3)

print(arr3)
