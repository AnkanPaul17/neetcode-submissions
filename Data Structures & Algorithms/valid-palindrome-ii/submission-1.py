class Solution:
    def validPalindrome(self, s: str) -> bool:
        lower_s=s.lower()
        good_s=""
        for ch in lower_s:
            if ch.isalnum():
                good_s+=ch
        l=0
        r=len(good_s)-1
        for i in range(len(good_s)//2):
            if good_s[l]!=good_s[r]:
                s1=good_s[l+1:r+1]
                s2=good_s[l:r]
                return s1==s1[::-1] or s2==s2[::-1]
            l+=1
            r-=1
        return True
        
        