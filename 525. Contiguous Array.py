"""Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap, res, cs = {}, 0, 0

        for index, ele in enumerate(nums, 1):
            if ele == 1:
                cs += 1
            else:
                cs -= 1
            if cs == 0:
                res = index-0
            if cs not in hashmap:
                hashmap[cs] = index
            else:
                res = max(res, index-hashmap[cs])
        return res
