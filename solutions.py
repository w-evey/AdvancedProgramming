class Solution:
    def twoSum(self, numbers, target):
        seen = {}

        for i, num in enumerate(numbers):
            pairCheck = target - num
            if pairCheck in seen:
                return[seen[pairCheck], i]
            seen[num] = i
    
    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
