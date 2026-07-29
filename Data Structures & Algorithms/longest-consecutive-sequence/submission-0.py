class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        count=0
        last_num=float("-inf")
        n=len(nums)
        nums.sort()
        for i in range(0,n):
            num=nums[i]
            if num-1==last_num:
                count+=1
            elif num!=last_num:
                count=1
            last_num=num
            max_len=max(max_len,count)
        return max_len
      