class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        response = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                response.append(newInterval)
                return response + intervals[i:]
            elif newInterval[0] > interval[1]:
                response.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]

        response.append(newInterval)
        return response
