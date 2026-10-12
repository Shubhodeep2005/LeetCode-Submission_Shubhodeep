class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        
        # Pair each number with its original index to track its position
        indices = [(num, i) for i, num in enumerate(nums)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
            
        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0  # Tracks how many elements from the right half are smaller
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    # Element from left side is placed: add all right-side elements seen so far
                    counts[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    # Element from right side is smaller: increment right_count
                    right_count += 1
                    merged.append(right[j])
                    j += 1
            
            # Append remaining elements
            while i < len(left):
                counts[left[i][1]] += right_count
                merged.append(left[i])
                i += 1
                
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        merge_sort(indices)
        return counts