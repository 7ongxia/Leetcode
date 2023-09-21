class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Write Index
        prev = None
        wi = 0
        k = 0

        for i in range(len(nums)):
            if prev != nums[i]:
                nums[wi] = nums[i]
                wi += 1
                k += 1
            prev = nums[i]

        return k