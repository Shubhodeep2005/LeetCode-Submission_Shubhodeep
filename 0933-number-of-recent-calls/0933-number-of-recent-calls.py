from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize an empty queue to store timestamps
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Step 1: Add the current timestamp to the queue
        self.requests.append(t)
        
        # Step 2: Remove all timestamps older than t - 3000 from the front
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
            
        # Step 3: The remaining items in the queue fall within [t - 3000, t]
        return len(self.requests)