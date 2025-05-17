class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_list = nums1 + nums2
        num_list.sort()

        if (len(num_list) % 2 == 1):
            mid = int((len(num_list) - 1) / 2)
            
            return num_list[mid]

        elif (len(num_list) % 2 == 0):
            mid = (len(num_list) - 1) / 2
            mid_left = int(mid - 0.5)
            mid_right = int(mid + 0.5)

            return (num_list[mid_left] + num_list[mid_right]) / 2