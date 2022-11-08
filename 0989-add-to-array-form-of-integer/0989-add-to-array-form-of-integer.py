class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = ''
        for d in num:
            number += str(d)
        
        added = int(number) + k
        
        result = []
        for d in str(added):
            result.append(d)
        
        return result