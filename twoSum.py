class Solution:
    def twoSum(self, numbers, target):
        seen = {}

        for i, num in enumerate(numbers):
            pairCheck = target - num
            if pairCheck in seen:
                return[seen[pairCheck], i]
            seen[num] = i
    

