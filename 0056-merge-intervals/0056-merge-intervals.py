class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 1. Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # 2. If merged is empty or current interval doesn't overlap, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 3. Otherwise, there is an overlap, merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged