class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        new_s=[]
        for i in range(n):
            if s[i]!=" ":
                new_s.append(s[i])
        fixed="".join(char for char in new_s if char.isalnum()).lower()
        rev_s=fixed[::-1]
        return rev_s==fixed


