class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            index_i=i
            complement=nums[i]
            for j in range(i+1,n):
                index_j=j
                if nums[j]==target-complement:
                    return [index_i,index_j]