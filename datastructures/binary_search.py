#Binary Search Algorithm

"""Approach

--> Sort the list
--> Compare k with the middle most element of the list.
--> If 'k' matches with the middle element then we return the mid index.
--> Else if 'k' is greater than the middle element then 'k' can only lie in the right half of the list after the middle element. So repeat the second and third step with the right half of the list.
--> Else if 'k' is smaller than the middle element repeat the second and thrid step with the left half of the list.
"""

li = [2,3,4,5,6,8]
k = 8
low = 0
high = len(li)-1
mid = 0

while low < high:

    mid = (low + high)//2

    if li[mid] < k:
        low = mid +1

    elif li[mid] > k:
        high = mid - 1

    else:
        print(mid)
