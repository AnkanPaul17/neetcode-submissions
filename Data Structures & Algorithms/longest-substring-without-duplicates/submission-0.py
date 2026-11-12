class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        length=0
        maxLength=0
        l=0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[l])
                l+=1
                length-=1
            length+=1
            maxLength=max(length, maxLength)
            ans.add(s[i])
        return maxLength

        