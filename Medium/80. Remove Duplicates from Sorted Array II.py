class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Base Case
        if len(nums) <= 2:
            return len(nums)

        length = len(nums)
        was_same = False
        r = len(nums) - 1  # right index
        l = len(nums) - 2  # left index

        for i in range(len(nums) - 1, 0, -1):
            if was_same and nums[l] == nums[r]:
                nums.pop(r + 1)

            if nums[l] == nums[r]:
                was_same = True
            else:
                was_same = False

            l -= 1
            r -= 1

        return len(nums)
