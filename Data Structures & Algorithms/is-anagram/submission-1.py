class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapp1,mapp2 = {},{}

        for i in range(len(s)):
            mapp1[s[i]] = 1 + mapp1.get(s[i],0)
            mapp2[t[i]] = 1 + mapp2.get(t[i],0)
        
        for c in mapp1:
            if mapp1[c] != mapp2.get(c,0):
                return False
        
        return True

        