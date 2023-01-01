class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n
        
        leftSum = 0
        for i in range(len(nums)):
            # 왼쪽합*2 == 전체합 - 현재 인덱스의 값
            if (leftSum*2 == total - nums[i]):
                return i
            leftSum += nums[i]

        return -1
