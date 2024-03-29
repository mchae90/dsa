class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            cs, ct = s[i], t[i]
            
            if (cs in mapST and mapST[cs] != ct) or (ct in mapTS and mapTS[ct] != cs):
                return False
            mapST[cs] = ct
            mapTS[ct] = cs
        
        return True

# Must check if both ST and TS map conflicts