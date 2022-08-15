class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i, j, k는 전부 다른 수
        # 각 값의 합은 0
        
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1
        
        return res