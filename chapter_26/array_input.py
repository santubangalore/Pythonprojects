from array import *

arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range (n):
    x= int(input("enter the next value"))
    arr.append(x)

print(arr)
