class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
            else:
                merged.append(intervals[i])
        
        return merged
            