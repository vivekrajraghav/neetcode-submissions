class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rev_freq_map={k:v for k,v in Counter(nums).items()}
        rev_freq_map=dict(sorted(rev_freq_map.items(), key=lambda item:item[1],reverse=True))
        result=list(rev_freq_map.keys())[:k]
        return result