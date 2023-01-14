class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for word in words:
            check = True
            copy = chars
            for w in word:
                print(word, w, copy, check)
                if w in copy:
                    copy = copy.replace(w, '', 1)
                else:
                    check = False
                    break
            
            if check:
                res += len(word)
        
        return res
