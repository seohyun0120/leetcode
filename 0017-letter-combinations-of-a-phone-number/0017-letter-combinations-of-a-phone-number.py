class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }

        if not digits:
            return []
        elif len(digits) == 1:
            return phone[digits]

        res = ['']
        for digit in digits:
            cur = []

            for up in phone[digit]:
                cur.extend(pre + up for pre in res)
            res = cur
        return res