from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in temp:
                return [temp[diff], index] 
            temp[num] = index
        return
