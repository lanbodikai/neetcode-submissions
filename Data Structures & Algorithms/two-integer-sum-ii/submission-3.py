class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1

        while i < n:
            sums = numbers[i] + numbers[n]

            if sums > target:
                n -= 1
            elif sums < target:
                i += 1
            else:
                return [i + 1, n + 1]
        
        return []