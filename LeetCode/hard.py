# 4. Median of Two Sorted Arrays
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        x = nums1 + nums2
        x.sort()
        if len(x)%2 == 0:
            i = len(x)//2
            p = (x[i] + x[i-1])/2
            return float(f"{p:.5f}")
        else:
            i = len(x)//2
            return float(f"{x[i]:.5f}")