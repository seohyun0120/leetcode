import math

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for d in digits:
            number += str(d)
        print(number)
        
        plus_one = int(number) + 1
        
        result = []
        for d in str(plus_one):
            result.append(d)
        
        return result