class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        
        self.back_tracking([])
        return self.res
        
    
    def back_tracking(self, current: List[int]):
        if len(current) == len(self.nums):
            self.res.append(current.copy())
            return
        
        for num in self.nums:
            if num in current:
                continue
            
            current.append(num)
            self.back_tracking(current)
            current.pop()