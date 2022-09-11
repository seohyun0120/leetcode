class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        for i, n in enumerate(nums):
            if n == target:
                return i