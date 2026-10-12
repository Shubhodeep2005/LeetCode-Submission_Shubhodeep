class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        def is_non_decreasing(arr: list[int]) -> bool:
            # Check if the array is already sorted in non-decreasing order
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        operations = 0
        
        # Keep simulating the operation until the array is fully sorted
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            min_idx = -1
            
            # Linearly scan to find the leftmost adjacent pair with the minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_idx = i
            
            # Replace the pair with their combined sum
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)
            
            operations += 1
            
        return operations