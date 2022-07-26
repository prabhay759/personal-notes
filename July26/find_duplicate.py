# Finding duplicates number in an array without using extra space
#
# All elements must be greater than 0
# Array size - n
# All elements of an array below or equal to n
# This code works on the basis of using index or index-1 and setting that value as negative


arr = [1, 6, 5, 2, 3, 3, 2]

for idx, x in enumerate(arr):
    index = abs(arr[idx])
    if arr[index] < 0:
         print('duplicate number', index)
    else:
        arr[index] = arr[index]*-1
