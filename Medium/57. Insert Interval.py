class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        new_start = newInterval[0]
        new_end = newInterval[1]

        new_interval = [None, None]
        is_start_found = False
        is_end_found = False
        merge_start = -1
        merge_end = -1

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if not is_start_found:
                if start <= new_start and end >= new_start:
                    merge_start = i
                    new_interval[0] = start
                    is_start_found = True
                elif start > new_start:
                    merge_start = i
                    new_interval[0] = new_start
                    is_start_found = True
                else:
                    merge_start = i + 1
                    new_interval[0] = new_start

            if not is_end_found:
                if new_end <= end and new_end >= start:
                    merge_end = i + 1
                    new_interval[1] = end
                    is_end_found = True
                elif new_end < start:
                    merge_end = i
                    new_interval[1] = new_end
                    is_end_found = True
                else:
                    merge_end = i + 1
                    new_interval[1] = new_end

        intervals[merge_start:merge_end] = [new_interval]
        return intervals
