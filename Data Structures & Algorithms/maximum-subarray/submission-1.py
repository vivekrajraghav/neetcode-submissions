class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        current_sum=0
        n=len(nums)
        for i in range(0,n):
            num=nums[i]
            current_sum+=num
            if max_sum<current_sum:
                max_sum=current_sum
            if current_sum<0:
                current_sum=0
        return max_sum