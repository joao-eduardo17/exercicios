# 75. Sort Colors
def sortColors(nums: list[int]) -> None:
        x = nums.copy()
        nums.clear()
        l1, l2 = [], []
        for c in x:
            if c == 0:
                nums.append(0)
            elif c == 1:
                l1.append(1)
            else:
                l2.append(2)
        nums += l1 + l2