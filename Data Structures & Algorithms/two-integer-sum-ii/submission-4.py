class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            right = len(numbers) - 1
            while right > i:
                if numbers[i] + numbers[right] == target:
                    return [i + 1, right + 1]
                else:
                    right -= 1