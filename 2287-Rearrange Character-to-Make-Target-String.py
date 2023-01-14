class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        smap = {}

        for c in s:
            if c in target:
                if not smap.get(c):
                    smap[c] = 1
                else:
                    smap[c] += 1

        res = 0
        while True:
            for c in target:
                if not smap.get(c) or smap[c] == 0:
                    return res
                else:
                    smap[c] -= 1

            res += 1
        return res
