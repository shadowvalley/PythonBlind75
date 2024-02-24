class Solution:
    # TC O(N) SC O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_answer = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                intervals_answer.append(interval)
            elif newInterval[1] < interval[0]:
                intervals_answer.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        intervals_answer.append(newInterval)
        return intervals_answer 