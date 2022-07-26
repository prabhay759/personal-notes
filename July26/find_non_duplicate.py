# Given an array where every element occurs three times, except one element which occurs only once.
# Find the element that occurs once. The expected time complexity is O(n) and O(1) extra space.


arr = [13, 19, 13, 13]
b = '' # max length would be 32

for index in range(0,32):
    sum = 0
    for idx, x in enumerate(arr):
        binary_number = "{0:032b}".format(x)
        sum += int(binary_number[index])
    b += str(sum%3)
print(int(b, 2))


# Explanations:
# Well described here:
# https://www.youtube.com/watch?v=jO7uGdvGGC4
