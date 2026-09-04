class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize the result array with 0s
        result = [0] * len(temperatures)
        
        # The stack will store INDICES of temperatures, not the temperatures themselves
        stack = [] 

        for i, current_temp in enumerate(temperatures):
            # While the stack is not empty AND the current day is warmer 
            # than the temperature at the index stored at the top of the stack
            while stack and temperatures[stack[-1]] < current_temp:
                # We found a warmer day for the index at the top of the stack!
                prev_day_index = stack.pop()
                
                # The number of days is the difference between the current index and previous index
                result[prev_day_index] = i - prev_day_index
            
            # Add the current day's index to the stack to wait for a warmer day
            stack.append(i)

        return result