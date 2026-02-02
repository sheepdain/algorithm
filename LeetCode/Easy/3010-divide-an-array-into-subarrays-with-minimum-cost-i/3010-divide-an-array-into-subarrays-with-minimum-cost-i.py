class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1, min_2=51,51
        for num in nums[1:]:
            if num<min_1:
                min_2=min_1
                min_1=num
            elif num==min_1:
                min_2=num
            else:
                if num<min_2:
                    min_2=num
        return nums[0]+min_1+min_2