class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        flug=0
        if nums[1]<nums[0]:
            return False
        for i in range(2, len(nums)):
            if nums[i]>nums[i-1]:
                if flug==1:
                    flug+=1
            elif nums[i]<nums[i-1]:
                if flug==0:
                    flug+=1
                elif flug==2:
                    return False
        if flug != 2:
            return False
        return True