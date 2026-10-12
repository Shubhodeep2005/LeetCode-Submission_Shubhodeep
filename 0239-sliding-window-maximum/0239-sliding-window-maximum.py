from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
      
        q = deque()  
        result = []
        
        for i, num in enumerate(nums):
            
            if q and q[0] < i - k + 1:
                q.popleft()
                
            while q and nums[q[-1]] < num:
                q.pop()
           
            q.append(i)
            
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result