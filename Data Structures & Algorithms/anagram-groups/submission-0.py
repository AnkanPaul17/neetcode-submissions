class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        freq={}
        for i in range(len(strs)):
            temp=[]
            sorted_str=''.join(sorted(strs[i]))
            if sorted_str not in freq:
                freq[sorted_str]=[]
            freq[sorted_str].append(strs[i])
        for i in freq:
            ans.append(freq[i])
        return ans
        



            
        