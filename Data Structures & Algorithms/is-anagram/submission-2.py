class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using Counter(s) == Counter(t)
        return Counter(s)==Counter(t)