class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        
        while i < n:
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
            
        intervals.insert(i, newInterval)
        
        result = [intervals[0]]
        
        for i in range(i, n+1):
            if intervals[i][0] > newInterval[1]:
                result.extend(intervals[i:])
                break
                
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
                continue
                
            if intervals[i][1] > result[-1][1]:
                result[-1][1] = intervals[i][1]
                       
        return result
        