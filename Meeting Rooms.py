class Solution:
    # TC O(NlogN) SC O(N) for tim sort
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        merged_intervals = []
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        for interval in sorted_intervals:
            if len(merged_intervals) == 0 or merged_intervals[-1][1] <= interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        print(f"{merged_intervals}")
        return True if len(merged_intervals) == len(intervals) else False 