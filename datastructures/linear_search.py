#Linear Search Algorithm

""" Approach
--> Start with the left most corner of the element list and compare one by one.
--> if the key element is found return the index of the element and break the loop.
--> If element is not found in the list return -1.

"""

#Implementation

li = [1, 2 , 9, 11, 15]

for i in range(len(li)):
    if li[i] == 9:
        print(i)
    else:
        print("Element not found in the list")

# Time Complexity is O(n)

"""It is not suitable as time complexity is big as for larger operation n is not preferred therefor we are going to use binary serach tree"""