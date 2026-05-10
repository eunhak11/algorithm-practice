"""
Given a list of integers and a target number,
return the indices of the two numbers that add up to the target.

You may assume exactly one solution exists
You cannot use the same element twice
Example:
nums = [2, 7, 11, 15], target = 9
→ return [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
"""

def two_sum(nums, target):
    seen = {}
    for i, val in enumerate(nums):
        need = target - val
        if need in seen:
            return [seen[need], i]
        seen[val] = i
        return None
    return None