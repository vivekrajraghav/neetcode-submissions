class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        smallest=float("inf")
        while high>=low:
            mid=(high+low)//2
            if nums[low]<=nums[mid]:
                smallest=min(smallest,nums[low])
                low=mid+1
            elif nums[high]>=nums[mid]:
                smallest=min(smallest,nums[mid])
                high=mid-1
        return smallest