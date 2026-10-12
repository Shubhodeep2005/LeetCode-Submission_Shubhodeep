class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        total_time = 0
        target_tickets = tickets[k]
        
        for i, t in enumerate(tickets):
            if i <= k:
                total_time += min(t, target_tickets)
            else:
                total_time += min(t, target_tickets - 1)
                
        return total_time