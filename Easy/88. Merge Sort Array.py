class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write_index = len(nums1) - 1
        pos1 = m - 1
        pos2 = n - 1

        while 0 <= pos2:
            if 0 <= pos1 and nums1[pos1] > nums2[pos2]:
                nums1[write_index] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[write_index] = nums2[pos2]
                pos2 -= 1
                
            write_index -= 1
