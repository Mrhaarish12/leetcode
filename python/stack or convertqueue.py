"""
Get a list of N user inputs such that first elemtns represents the bottom of the stack. you need to pop k elements from the stack. If k is greater than n, convert the stack into a queue. the bottom of the stack represents the fron of the queue. You have to enqueue exacktly k elements intot the queue and print the queue."""

n = int(input("Enter the size of the stack: "))

items = []
for i in range(n):
    ele = int(input(f"Enter the item number:{i+1} "))
    items.append(ele)

k = int(input("Enter the number of operations to be performered:"))

if k<n:
    #if k is less than n, then the stack is there
    for i in range(k):
        items.pop()
else:
    print("k is greater than n, therefore it is converted into stack")
    for i in range(k):
        ele = int(input(f"Enter the element number: {i+1} to enqueue: "))
        items.append(ele)

print(items)