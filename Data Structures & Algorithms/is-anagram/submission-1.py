class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tb={}
        if len(s)!=len(t):
            return False
        for ch in s:
            tb[ch] = tb.get(ch,0)+1
        for ch in t:
            if ch not in tb:
                return False
            else:
                tb[ch] = tb.get(ch,0)-1
        for ch in tb:
            if tb.get(ch)!=0:
                return False
        return True