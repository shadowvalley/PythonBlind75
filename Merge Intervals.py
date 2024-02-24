class Solution:
    # TC O(NlogN) SC O(N) for tim sort
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        sorted_intervals = sorted(intervals, key = lambda x:x[0])

        for interval in sorted_intervals:
            if len(merged_intervals) == 0 or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        return merged_intervals