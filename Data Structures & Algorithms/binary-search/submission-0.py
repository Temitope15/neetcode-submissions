class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1 #5
        while start <= end:
            m = start + (end - start) //2 #0+(5)//2 = 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                start = m + 1 #3
            else:
                end = m -1
        return -1