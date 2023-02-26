class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metal = 0
        paper = 0
        glass = 0

        m = 0
        p = 0
        g = 0

        for idx, x in enumerate(garbage):
            if 'M' in x:
                metal = idx
                m += x.count('M')
            if 'G' in x:
                glass = idx
                g += x.count('G')
            if 'P' in x:
                paper = idx
                p += x.count('P')

        if metal:
            for i in range(metal):
                m += travel[i]
        if glass:
            for i in range(glass):
                g += travel[i]
        if paper:
            for i in range(paper):
                p += travel[i]
        return m+g+p