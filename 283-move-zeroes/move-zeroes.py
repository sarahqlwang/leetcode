class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeelements(nums, 0)
        for i in range(p, len(nums)):
            nums[i] = 0


    def removeelements(self, nums, val):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast+=1
        return slow
        