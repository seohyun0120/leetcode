class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []

        sum = 0
        for n in nums:
            sum = sum+n
            ans.append(sum)
        
        return ans
