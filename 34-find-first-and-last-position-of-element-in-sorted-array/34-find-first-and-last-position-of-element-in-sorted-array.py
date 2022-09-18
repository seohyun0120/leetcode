class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        if len(nums) == 1:
            return [0, 0]
        
        def binarySearch(target):
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        left = binarySearch(target)
        right = binarySearch(target+1) - 1
        
        return [left, right]