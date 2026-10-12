class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        
        for i, water_needed in enumerate(plants):
            if current_water >= water_needed:
              
                steps += 1
                current_water -= water_needed
            else:
                steps += 2 * i + 1
                current_water = capacity - water_needed
                
        return steps