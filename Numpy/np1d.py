#! /usr/bin/env python3

# Q. Import numpy as np and print the version number.
import numpy as np
print(np.__version__)


# Q. Create a 1D array of numbers from 0 to 9
a = np.arange(10)

# Q. Create a 3×3 numpy array of all True’s
a = np.full((3,3),True,dtype=bool)
a = np.ones((3,3),dtype=bool)

# Q. Extract all odd numbers from arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 !=0]

#Q. Replace all odd numbers in arr with -1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 !=0] = -1

# Q. Replace all odd numbers in arr with -1 without changing arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr%2!=0,-1,arr)

# Q. Convert a 1D array to a 2D array with 2 rows
a = np.arange(10).reshape(2,-1)

# Q. Stack arrays a and b vertically
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

np.r_[a,b]
np.vstack([a,b])
np.concatenate([a,b],axis=0)

# Q. Stack the arrays a and b horizontally.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

np.c_[a,b]
np.hstack([a,b])
np.concatenate([a,b],axis=1)


# Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1,2,3])
np.r_[np.repeat(a,3),np.tile(a,3)]
out = [np.repeat(a,3),np.tile(a,3)]
np.concatenate(out)
np.hstack(out)

# Q. Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

# Q. From array a remove all items present in array b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

np.setdiff1d(a,b)

# Q. Get the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a==b)


# Q. Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
mask = (a>=5) & (a<=10)
a[mask]
a[np.where(mask)]

#Q. Convert the function maxx that works on two scalars, to work on two arrays.
def maxx(x, y):
    """Get the maximum of two items"""
    return np.max([x,y],axis=0)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

maxx(a,b)


# Q. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)
arr = arr[:,[1,0,2]]


# Q. Swap rows 1 and 2 in the array arr
arr = np.arange(9).reshape(3,3)
arr = arr[[1,0,2]]


# Q. Reverse the rows of a 2D array arr.
arr = np.arange(9).reshape(3,3)
arr = arr[::-1]


# Q. Reverse the columns of a 2D array arr.
arr = np.arange(9).reshape(3,3)
arr = arr[:,::-1]

