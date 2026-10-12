from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        #Convert all integers to strings
        num_strs = list(map(str, nums))
        
        #Custom comparator functio
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
        
        #Sort using the custom comparator
        num_strs.sort(key=cmp_to_key(compare))
        
        #Join the sorted numbers into a single string
        result = "".join(num_strs)
        
        #Edge case: If the largest number is "0", return "0" instead of "000..."
        return "0" if result[0] == "0" else result