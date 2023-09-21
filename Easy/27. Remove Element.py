class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Right index
        ri = len(nums) - 1
        # Left index
        li = 0
        k = 0

        while li <= ri:
            if nums[li] == val:
                nums[li] = nums[ri]
                nums[ri] = None
                ri -= 1
                k += 1
            else:
                li += 1
        
        return len(nums) - k