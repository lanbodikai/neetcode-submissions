class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        times = []
        count = 0

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            times.append((position[i], time))
        
        times.sort(reverse = True)

        for j, time in times:
            if not stack:
                count += 1
                stack.append(time)
            elif time > stack[-1]:
                count += 1
                stack.append(time)
        

        return count
        

        
