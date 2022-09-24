#달팽이 알고리즘

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        
        num = 1
        start = 0
        while n > 0:
            num = self.outer(res, start, n, num)
            n -= 2
            start += 1
        
        return res
        
    
    def outer(self, res, start, size, num):
        last = start + size - 1

        # 첫째행 처리(가장 상단줄)
        for c in range(start, last+1):
            res[start][c] = num
            num+=1
        
        # 마지막열 처리(우측)
        for r in range(start+1, last+1):
            res[r][last] = num
            num += 1
        # 마지막행 처리 (가장 하단줄)
        for c in range(last-1, start-1, -1):
            res[last][c] = num
            num +=1
        
        # 첫번째열 처리(좌측)
        for r in range(last-1, start, -1):
            res[r][start] = num
            num += 1
        
        # 가장 마지막에 넣은 숫자 추가
        return num