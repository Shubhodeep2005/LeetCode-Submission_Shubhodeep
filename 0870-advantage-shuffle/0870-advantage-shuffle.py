class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
      
        nums1.sort()
    
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: x[1], reverse=True)
     
        left, right = 0, len(nums1) - 1
        res = [0] * len(nums1)
        
        for original_idx, val in sorted_nums2:
            if nums1[right] > val:

                res[original_idx] = nums1[right]
                right -= 1
            else:
                
                res[original_idx] = nums1[left]
                left += 1
                
        return res