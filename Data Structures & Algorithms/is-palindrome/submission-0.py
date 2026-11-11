class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s=s.lower()
        good_s=""
        for ch in lower_s:
            if ch.isalnum():
                good_s+=ch
        l=0
        r=len(good_s)-1
        for i in range(len(good_s)//2):
            if good_s[l]!=good_s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        