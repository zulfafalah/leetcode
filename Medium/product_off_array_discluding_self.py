# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# prefix : [1, 2, 6, 24]

# sufix : [24, 24, 12, 4]

# result = [24, 12, 8, 6]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            print(nums[i+1])



if __name__ == '__main__':
    nums = [1,2, 3, 4]
    solution = Solution()
    res = solution.productExceptSelf(nums)
    print(res)