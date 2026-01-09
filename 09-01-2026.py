# Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer.
#  If the target is found in the array, return its index. If the target is not found, return -1.

nums = list(map(int, input("Enter sorted numbers (comma-separated): ").split(',')))
target = int(input("Enter target: "))

n = len(nums)
low = 0
high = n - 1
ind = -1  # Initialize before function

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] == target:
        ind = mid
        break  # Found it, exit loop
    elif target < nums[mid]: 
        high = mid - 1        
    else:
        low = mid + 1

if ind == -1:
    print("The target is not present.")
else:
    print("The target is at index:", ind)