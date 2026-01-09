# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

def lower_bound(nums, x):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

# Interactive version
nums = list(map(int, input("Enter sorted numbers (comma-separated): ").split(',')))
x = int(input("Enter x: "))
idx = lower_bound(nums, x)

if idx == len(nums):
    print(f"x is greater than all elements. Lower bound: {idx}")
elif nums[idx] == x:
    print(f"First occurrence of x is at index: {idx}")
else:
    print(f"Lower bound of x is at index: {idx} (nums[{idx}] = {nums[idx]})")
