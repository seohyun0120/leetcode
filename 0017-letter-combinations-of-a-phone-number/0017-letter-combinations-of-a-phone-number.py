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

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return phone[digits]

        res = ['']
        for digit in digits:
            cur = list()
            
            for up in phone[digit]:
                for pre in res:
                    cur.append(pre + up)
            res = cur
        return res