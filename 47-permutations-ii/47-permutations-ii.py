class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        # 현재 숫자 사용 여부
        used = [False for i in range(len(nums))]

        nums.sort()

        # backtrack
        def backtrack(nums):
            # 길이가 같을 경우 정답
            if len(track) == len(nums):
                res.append(list(track))
                return

            # 이미 사용된 숫자면 건너뜀
            for i in range(len(nums)):
                if used[i] is True:
                    continue

                # 이전 숫자와 같으면 이미 사용했다고 판단
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue

                track.append(nums[i])
                used[i] = True

                backtrack(nums)

                track.pop(-1)
                used[i] = False


        backtrack(nums)
        return res