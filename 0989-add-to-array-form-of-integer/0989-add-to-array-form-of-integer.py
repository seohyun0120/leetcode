class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = ''.join(str(d) for d in num)
        added = int(number) + k

        return list(str(added))