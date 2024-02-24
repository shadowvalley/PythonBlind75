class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time, end_time = [], []

        for interval in intervals:
            start_time.append(interval[0])
            end_time.append(interval[1])

        # sort 
        start_time.sort() 
        end_time.sort() 

        # logic 
        roomsCount = 0
        max_rooms = 0
        i, j = 0, 0
        while i < len(start_time):
            if start_time[i] < end_time[j]:
                roomsCount += 1
                i+=1
            else:
                roomsCount -= 1
                j+=1
            max_rooms = max(max_rooms, roomsCount)
        return max_rooms