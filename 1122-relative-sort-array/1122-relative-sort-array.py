class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        
        count = [0] * 1001
        for num in arr1:
            count[num] += 1
            
        result = []
        
        for num in arr2:
            while count[num] > 0:
                result.append(num)
                count[num] -= 1
                
       
        for num in range(len(count)):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1
                
        return result