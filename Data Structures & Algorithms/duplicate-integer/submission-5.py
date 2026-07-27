class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using Hash Map
        # n=len(nums)
        # is_duplicate=False
        # hash_map={}
        # for i in range(0,n):
        #     hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        # for key in hash_map:
        #     if hash_map[key]>1:
        #         return True
        # return is_duplicate

        # Using Hash Set
        return len(set(nums))!=len(nums)