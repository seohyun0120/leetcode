import math

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(str(d) for d in digits)
        print(number)

        plus_one = int(number) + 1

        return list(str(plus_one))