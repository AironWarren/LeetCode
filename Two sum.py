"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
nums = [1, 4, 5, 7]
target = 9
a = 0
b = 0
for item in nums:
    for item2 in nums[(nums.index(item) + 1):]:
        if (item + item2) == target:
            a = item
            b = item2
            break
    if (a + b) == target:
        break
if a == b:
    ans = [nums.index(a), nums.index(b, 1)]
    print('[{0},{1}]'.format(ans[0], ans[1]))
    # return ans
else:
    ans = [nums.index(a), nums.index(b)]
    print('[{0},{1}]'.format(ans[0], ans[1]))
    # return ans

