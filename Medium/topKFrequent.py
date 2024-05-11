from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        if len(nums) == 1:
            return nums

        for i in nums:
            if i not in temp:
                temp[i] = 1

            else:
                temp[i] += 1

        a = dict(sorted(temp.items(), key=lambda item: item[1], reverse=1))
        b = list(a.keys())
        return b[:k]
