class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = -inf
        cur_max = 0      

        for i in nums:
            cur_max = max(cur_max + i, i)
            
            if cur_max > res:
                res = cur_max
            
        return res