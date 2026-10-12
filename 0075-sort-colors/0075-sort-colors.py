class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap 0 to the front (low boundary)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                #1 is already in the middle, just move forward
                mid += 1
            else:  # nums[mid] == 2
                #Swap 2 to the back (high boundary)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1