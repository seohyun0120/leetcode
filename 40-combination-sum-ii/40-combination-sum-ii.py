class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        self.dfs(candidates, 0, [], result, target)
        return result
        
    def dfs(self, nums, idx, path, res, target):
        if not target:
            res.append(path)
            return

        for i in range(idx, len(nums)):
            # 중복 원소 제거
            if i > idx and nums[i] == nums[i-1]:
                continue

            # target보다 클 경우 break
            if nums[i] > target:
                break

            self.dfs(nums, i+1, path + [nums[i]], res, target-nums[i])