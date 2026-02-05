class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                res = nums[(i + nums[i]) % n]
                result[i] = res
        return result